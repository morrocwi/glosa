"""glosa kernel — schemas -> kernel -> CLI -> MCP -> plugin callable layer.

tier: finite_diagnostic (tests executed: `python3 -m unittest discover -s tests -v`, run from
the glosa repo root). Every function below is mechanically checked by `tests/test_kernel.py`
against the valid examples and the six deliberate-FAIL fixtures in `schema/examples/fail/`.
Anything this file's docstrings describe but the test suite does not exercise is NOT covered by
that tier claim -- readout-not-truth applies to this file's own header too.

Implements FOUNDATION_v0.5.md §9 ("Callable layer"), the 12 kernel gate rules of §3.3 (11
original + rule 12, D-LENS-UNSIGNED, MUST-6), the independence ladder of §4.2, the genre router
of §6.3b, the disclaimer catalogue lookup of §5, the citation-integrity / release-gate machinery
of §7.4/§7.8, and the MC-01 human-Approver-identity extension (MUST-7, ARCH_integrity.md F1).

One-fact-one-home (FOUNDATION §8): every field name this module reads is DEFINED in
`schema/*.schema.json`, never redeclared here (fields this module reads that a schema does not
yet formally declare as a named property -- e.g. `independent_check.approver_kind`,
`lens_translation.lens_ref`, `hypothesis_world.signature` -- are legal additional data under
every relevant schema's own `additionalProperties: true`/unset default; declaring them formally
in the schema itself is a separate, out-of-scope-for-this-fix task). This module is stdlib-only
-- `json`, `pathlib`, `datetime`, `re`, `sys` -- with `jsonschema` imported OPTIONALLY behind a
try/except.

MUST-4 (fail-closed schema validation): when `jsonschema` cannot be imported (or a named schema
file is missing from the store), every `validate_*` function below now FAILS CLOSED by default --
returns `ok: False` with a plain "jsonschema not available; schema validation not performed"
error -- instead of silently degrading to the coarse presence-only fallback check and reporting
`ok: True` on an illegitimate payload (the exact F1/F3 findings in `reviews/ARCH_integrity.md`).
A caller that has a real reason to accept the coarse check anyway may pass
`allow_no_jsonschema=True`; the Result's `tier` is then downgraded to `Dr` (never
`finite_diagnostic`) and a warning records that the caller explicitly opted in. See
`_schema_validate_gated` below.

The kernel never adjudicates truth, only structure (task instruction, restated here because it
governs every design choice in this file): every hard-fail below is a SHAPE/PRESENCE/STRUCTURAL
check, or a lexical/regex heuristic explicitly labeled as such. No function here decides whether
a claim is actually correct.

No network call anywhere in this file (FOUNDATION §9: "no network call inside a
validate_*/gate_release/defeater_route function").
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

try:
    import jsonschema  # type: ignore
    from jsonschema import Draft7Validator, RefResolver  # type: ignore

    _HAVE_JSONSCHEMA = True
except Exception:  # pragma: no cover - exercised only in an environment without jsonschema
    jsonschema = None  # type: ignore
    _HAVE_JSONSCHEMA = False


# --------------------------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "schema"
DISCLAIMER_CATALOGUE_PATH = REPO_ROOT / "methodology" / "data" / "disclaimer_catalogue.json"


# --------------------------------------------------------------------------------------------
# Result — the one shape every validate_*/gate-ish function returns (task instruction)
# --------------------------------------------------------------------------------------------

def _result(ok, verdict=None, errors=None, warnings=None, tier="finite_diagnostic"):
    """Build the standard {ok, verdict, errors, warnings, tier} Result object.

    `tier` describes the KERNEL CHECK's own status (mechanical, executed, tested here), never
    the underlying claim's truth -- the kernel never adjudicates truth, only structure. Every
    Result this module returns is `finite_diagnostic` unless a heuristic (lexical/regex) check
    was the ONLY thing that produced a warning/error, in which case that specific
    warning/error string is prefixed `HEURISTIC:` so a caller can see which findings are
    structural (exact) and which are a lexical proxy (schema/README.md's own admitted limit,
    "free-text semantic scanning ... left to the kernel's actual text-processing code").
    """
    errors = list(errors or [])
    warnings = list(warnings or [])
    if verdict is None:
        if errors:
            verdict = "FAIL"
        elif warnings:
            verdict = "PASS_WITH_LIMITS"
        else:
            verdict = "PASS"
    return {
        "ok": bool(ok) and not errors,
        "verdict": verdict,
        "errors": errors,
        "warnings": warnings,
        "tier": tier,
    }


# --------------------------------------------------------------------------------------------
# Schema loading + validation (jsonschema optional, per task instruction)
# --------------------------------------------------------------------------------------------

_SCHEMA_STORE = None  # lazy cache: {$id: schema_dict}


def _load_schema_store():
    """Load every schema/*.schema.json + common.defs.json into a {$id: schema} store.

    Mirrors schema/README.md's own documented pattern exactly (RefResolver + store), since a
    bare `jsonschema.validate()` cannot resolve the cross-file `$ref`s this repo's schemas use.
    Returns None if the schema/ directory is not present or jsonschema is unavailable -- callers
    fall back to `_fallback_required_check`.
    """
    global _SCHEMA_STORE
    if _SCHEMA_STORE is not None:
        return _SCHEMA_STORE
    if not _HAVE_JSONSCHEMA or not SCHEMA_DIR.is_dir():
        _SCHEMA_STORE = {}
        return _SCHEMA_STORE
    store = {}
    for p in list(SCHEMA_DIR.glob("*.schema.json")) + [SCHEMA_DIR / "common.defs.json"]:
        if not p.is_file():
            continue
        try:
            schema = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if "$id" in schema:
            store[schema["$id"]] = schema
    _SCHEMA_STORE = store
    return store


def _validator_for(schema_filename):
    """Return a Draft7Validator wired with a RefResolver for the named schema file, or None."""
    store = _load_schema_store()
    schema_id = f"https://glosa.example/schema/{schema_filename}"
    schema = store.get(schema_id)
    if schema is None:
        return None
    resolver = RefResolver(base_uri=schema["$id"], referrer=schema, store=store)
    return Draft7Validator(schema, resolver=resolver)


# Minimal required-field fallback tables, hand-mirrored from each schema's own top-level
# "required" array (used ONLY when jsonschema is not importable or schema/ is missing -- this
# is deliberately a coarse presence check, never a substitute for the real schema when it is
# available; task instruction: "jsonschema may be imported OPTIONALLY ... with a fallback
# minimal required-field check").
_FALLBACK_REQUIRED = {
    "claim_card.schema.json": [
        "claim_id", "shape", "statement", "standpoint", "claim_type", "tier",
        "produced_by", "responsible", "origin_blackbox_ref", "five_questions",
        "non_claims", "human_owner", "status",
    ],
    "review_report.schema.json": [
        "claim_ref", "route_id", "independence_class", "role", "verdict", "verdict_tier",
        "reviewer_identity", "date",
    ],
    "citation_card.schema.json": [
        "id", "claim_ref", "identifier", "fetch_status", "metadata_verified",
        "claim_match_verified", "scope", "independence_class", "status",
    ],
    "release_manifest.schema.json": [
        "manifest_id", "artifact_refs", "gate_verdict", "adversarial_review", "status",
        "blackbox_note_appendix_present", "human_owner",
    ],
    "blackbox_note.schema.json": [
        "id", "project", "participants", "language", "privacy_scan", "lines", "cooking",
    ],
}


def _fallback_required_check(instance, schema_filename):
    """Coarse presence-only check: every top-level required key is present and non-None."""
    errors = []
    for key in _FALLBACK_REQUIRED.get(schema_filename, []):
        if key not in instance or instance[key] is None:
            errors.append(f"fallback-check: missing required field '{key}'")
    return errors


def _schema_validate(instance, schema_filename):
    """Validate `instance` against schema/<schema_filename>.

    Returns (errors: [str], used_fallback: bool). Tries the real jsonschema-backed validator
    first; falls back to `_fallback_required_check` (and says so) when jsonschema is not
    importable or the schema store could not be built.
    """
    validator = _validator_for(schema_filename)
    if validator is not None:
        errors = [f"{'/'.join(str(p) for p in e.path) or '(root)'}: {e.message}" for e in validator.iter_errors(instance)]
        return errors, False
    return _fallback_required_check(instance, schema_filename), True


def _schema_validate_gated(instance, schema_filename, allow_no_jsonschema):
    """MUST-4 shared fail-closed wrapper around `_schema_validate`.

    When the real jsonschema-backed validator ran (`used_fallback` False), this is a pass-through:
    the schema's own errors, no warnings, tier stays `finite_diagnostic`. When it silently fell
    back to the coarse presence-only check (`used_fallback` True -- jsonschema not importable, or
    `schema/<schema_filename>` missing from the store), `allow_no_jsonschema` decides what
    happens:

    - False (the default): FAIL CLOSED. Every rule encoded only in the schema's own `allOf` was
      NOT run this call -- returning `ok: True` here would repeat exactly the silent-degrade
      finding `reviews/ARCH_integrity.md` F1/F3 reproduced live (an illegitimate K2/Th_coqc/
      Approved-for-Live payload passing with `ok: True` the moment `jsonschema` import fails). One
      plain, unambiguous error is appended -- never a buried warning a caller's exit code ignores.
    - True: the caller has explicitly accepted the coarse fallback check as sufficient for this
      call. The tier is downgraded to `Dr` (never `finite_diagnostic` -- a presence-only pass is a
      judgment call, not a mechanically-verified one) and a warning records the opt-in.

    Returns (errors: [str], warnings: [str], tier: str, used_fallback: bool).
    """
    schema_errors, used_fallback = _schema_validate(instance, schema_filename)
    errors = list(schema_errors)
    warnings = []
    tier = "finite_diagnostic"
    if used_fallback:
        if allow_no_jsonschema:
            tier = "Dr"
            warnings.append(
                f"jsonschema not available -- ran only the minimal required-field fallback check "
                f"for {schema_filename}; caller explicitly accepted this via "
                "allow_no_jsonschema=True (MUST-4), so the result tier is downgraded to Dr, "
                "never finite_diagnostic."
            )
        else:
            errors.append("jsonschema not available; schema validation not performed")
    return errors, warnings, tier, used_fallback


# --------------------------------------------------------------------------------------------
# Kernel-only rules that JSON Schema draft-07 cannot express
# (schema/README.md's own table: rules 5, 6, 8 are fully kernel-only; rules 4 and 9's bounded
# I2+I4 90-day arithmetic is kernel-only too)
# --------------------------------------------------------------------------------------------

_ADVANCED_STATUSES = {"Approved-for-Test", "Approved-for-Live", "Monitor", "Rollback"}

# Kernel rule 8 (§3.3): phrases that PROPOSE external/institutional validation as a legitimacy
# lever (EPIS-KNOWLEDGE-VALIDATION). This is deliberately narrower than the disclaimer
# catalogue's D-NO-VERTICAL-AUTHORITY trigger (which fires on any MENTION of peer
# review/venue/institutional accept-reject) -- rule 8 fires only on phrasing that proposes such
# a thing as what would make the claim MORE legitimate. A lexical heuristic, tagged as such;
# schema/README.md names this class of check ("free-text semantic scanning") as permanently
# out of JSON Schema's reach and explicitly kernel-only.
_EXTERNAL_VALIDATION_PROPOSED_PATTERNS = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"external\s+validation",
        r"outside\s+validation",
        r"get\s+(an?\s+)?(outside|external)\s+(physicist|expert|reviewer|review)",
        r"seek(ing)?\s+external\s+(review|validation|certification)",
        r"(would|will|to)\s+(legitimi[sz]e|make\s+this\s+(more\s+)?legitimate)",
        r"institutional\s+recognition\s+(would|to)\s+(confirm|legitimi[sz]e|validate)",
        r"peer\s+review(ed)?\s+(would|to)\s+(confirm|legitimi[sz]e|validate)",
        r"requires?\s+(outside|external)\s+(validation|certification|endorsement)",
    ]
]


def _scan_for_external_validation_proposed(card):
    """Kernel rule 8 (§3.3): hard-fail text scan across statement/assumed[].description/ledger.*.

    Returns a list of (field_path, matched_text) hits. Empty list = clean.
    """
    hits = []

    def _check(path, text):
        if not isinstance(text, str):
            return
        for pat in _EXTERNAL_VALIDATION_PROPOSED_PATTERNS:
            m = pat.search(text)
            if m:
                hits.append((path, m.group(0)))

    stmt = (card.get("statement") or {})
    _check("statement.text", stmt.get("text"))
    translation = stmt.get("translation") or {}
    _check("statement.translation.text", translation.get("text"))

    for i, a in enumerate((card.get("five_questions") or {}).get("assumed") or []):
        _check(f"five_questions.assumed[{i}].description", (a or {}).get("description"))

    ledger = card.get("ledger") or {}
    for bucket in ("forced", "borrowed", "open"):
        for i, entry in enumerate(ledger.get(bucket) or []):
            _check(f"ledger.{bucket}[{i}]", entry)

    return hits


def mc01_check(maker, checker, approver):
    """MC-01 (§7.2): maker, checker, approver must be pairwise distinct, non-empty strings.

    Returns a Result. This is the exact-structural half of §3.3 rule 5 -- string-inequality
    across three fields, which schema/README.md names as permanently outside JSON Schema
    draft-07's reach ("no 'these three fields must differ pairwise'").
    """
    errors = []
    ids = {"maker_id": maker, "checker_id": checker, "approver_id": approver}
    for name, value in ids.items():
        if not value or not isinstance(value, str) or not value.strip():
            errors.append(f"mc01: {name} is missing/empty")
    present = {k: v for k, v in ids.items() if isinstance(v, str) and v.strip()}
    seen = {}
    for name, value in present.items():
        if value in seen:
            errors.append(f"mc01: {name} == {seen[value]} ('{value}') -- MC-01 requires pairwise distinct identities")
        else:
            seen[value] = name
    return _result(ok=not errors, errors=errors)


def _mc01_errors_for_card(card):
    """Kernel rule 5 (§3.3): MC-01 applies once `status` has advanced past 'Pending Review'."""
    status = card.get("status")
    if status not in _ADVANCED_STATUSES:
        return []
    ic = card.get("independent_check") or {}
    res = mc01_check(ic.get("maker_id"), ic.get("checker_id"), ic.get("approver_id"))
    return [f"rule5(MC-01): {e}" for e in res["errors"]]


# --------------------------------------------------------------------------------------------
# MUST-7: MC-01 human-identity extension -- pairwise string-distinctness (above) is necessary
# but not sufficient; nothing previously checked whether any of maker/checker/approver actually
# NAMES A HUMAN. reviews/ARCH_integrity.md F1 reproduced three distinct AI-vendor session strings
# reaching tier:Th_coqc, k_state:K2, status:Approved-for-Live with ok:True and zero disclaimer
# naming the missing human. FOUNDATION_v0.5.md §7.1's L3/L5 table requires "a distinct human
# Approver" at L3 and an "I5 (independent external human, non-founder)" check at L5 -- prose
# requirements with no prior field/check anywhere. The mechanism chosen here (per task
# instruction): read `approver_kind` (an enum "human"|"ai" the templates fixer is adding to
# review_report.schema.json/release_manifest.schema.json) wherever it sits alongside an
# independent-check block, and hard-fail once the artifact reaches a gate that legally requires
# a human. `approver_kind` is legal additional data on claim_card.independent_check too under
# that schema's own unset-default additionalProperties (see module docstring) even though the
# templates fixer's task did not name claim_card specifically -- the claim_card is where F1's own
# exploit landed, so leaving it uncovered would not close the finding that motivated this fix.
# --------------------------------------------------------------------------------------------

_HUMAN_APPROVER_REQUIRED_K_STATES = {"K2", "K3"}


def _human_approver_error_for_card(card):
    """MUST-7: once a claim_card's `status` reaches Approved-for-Live, or its `k_state` reaches
    K2/K3 with a completed (`independent_check.status == "PASSED"`) independent check on file, or
    its `independent_check.mc_level` reaches L5, `independent_check.approver_kind` must be
    present and exactly "human" -- an AI identity string, however distinct from maker/checker
    (rule 5/MC-01 above), never satisfies the Approver role (FOUNDATION §7.1 L3/L5; AGENTS.md rule
    5, "AI is never an author"). The K2/K3 leg is deliberately narrower than a bare `k_state`
    check: `k_state` alone can be set on a scratch/isolation payload with no independent check
    performed at all (`independent_check.status == "NONE"`, as `KernelRuleIsolationTest`'s own
    rule-4 isolation case does to test rule 4 in isolation) -- there is no Approver identity to
    validate yet in that state, so this rule stays silent until an actual PASSED check exists,
    consistent with rule 5/MC-01 above only firing once `status` has itself moved past a draft-ish
    state. Returns an error string, or None when the gate does not apply or is satisfied.
    """
    status = card.get("status")
    k_state = card.get("k_state")
    ic = card.get("independent_check") or {}
    mc_level = ic.get("mc_level")
    gated = (
        status == "Approved-for-Live"
        or (k_state in _HUMAN_APPROVER_REQUIRED_K_STATES and ic.get("status") == "PASSED")
        or mc_level == "L5"
    )
    if not gated:
        return None
    approver_kind = ic.get("approver_kind")
    if approver_kind != "human":
        return (
            "MC-01-HUMAN(claim_card): status/k_state/mc_level requires a human Approver "
            f"(status={status!r}, k_state={k_state!r}, mc_level={mc_level!r}) but "
            f"independent_check.approver_kind is {approver_kind!r}, not 'human' -- an AI "
            "identity never satisfies the Approver role at Approved-for-Live/K2/K3/L5 "
            "(FOUNDATION §7.1)."
        )
    return None


def _human_approver_error_for_review(report):
    """MUST-7: once a review_report's own `mc_level` reaches L5, or its `independence_class` is
    I5 ("independent external human, non-founder", FOUNDATION §7.1), the check itself must
    actually have been performed by a human -- `approver_kind` must be present and exactly
    "human". Class-5-never-substitutes-for-I5 (§7.1): no AI reviewer_identity, however
    cross-vendor-independent, satisfies an I5/L5 requirement. Returns an error string or None.
    """
    mc_level = report.get("mc_level")
    independence_class = report.get("independence_class")
    gated = mc_level == "L5" or independence_class == "I5"
    if not gated:
        return None
    approver_kind = report.get("approver_kind")
    if approver_kind != "human":
        return (
            "MC-01-HUMAN(review_report): mc_level/independence_class requires a human check "
            f"(mc_level={mc_level!r}, independence_class={independence_class!r}) but "
            f"approver_kind is {approver_kind!r}, not 'human'."
        )
    return None


def _human_approver_error_for_manifest(manifest):
    """MUST-7: once a release_manifest's `status` reaches Approved-for-Live, or
    `k_state_declared` reaches K2/K3, or `independent_check_summary.mc_level` reaches L5,
    `independent_check_summary.approver_kind` must be present and exactly "human". Returns an
    error string or None.
    """
    status = manifest.get("status")
    k_state = manifest.get("k_state_declared")
    ics = manifest.get("independent_check_summary") or {}
    mc_level = ics.get("mc_level")
    gated = (
        status == "Approved-for-Live"
        or k_state in _HUMAN_APPROVER_REQUIRED_K_STATES
        or mc_level == "L5"
    )
    if not gated:
        return None
    approver_kind = ics.get("approver_kind")
    if approver_kind != "human":
        return (
            "MC-01-HUMAN(release_manifest): status/k_state_declared/mc_level requires a human "
            f"Approver (status={status!r}, k_state_declared={k_state!r}, mc_level={mc_level!r}) "
            f"but independent_check_summary.approver_kind is {approver_kind!r}, not 'human'."
        )
    return None


# Rule 6 (§3.3): "scope.claim_scope may not exceed scope.evidence_scope" -- a free-text
# containment check schema/README.md itself calls "string-containment/human-reviewed". The
# kernel's job is structure, not truth, so this is implemented as a STRUCTURAL proxy over the
# two strings plus `scope.generalization_claimed`, not a semantic judgment of whether the claim
# is actually correct at that scope.
_BROADENING_MARKERS = re.compile(
    r"\b(all|every|generally|in general|universal(ly)?|population|everyone|always)\b", re.IGNORECASE
)
_SINGLE_SUBJECT_MARKERS = re.compile(
    r"\b(n\s*=\s*1\b|one\s+(household|cat|case|subject|person)|single[- ](subject|case))\b",
    re.IGNORECASE,
)


def _scope_exceeds_evidence(scope):
    """Structural proxy for rule 6. Returns a reason string if `claim_scope` looks broader than
    `evidence_scope`, else None. Two independent structural signals, either one is a hard fail:

    (a) claim_scope names a broadening marker (all/every/population/...) that evidence_scope does
        not also name;
    (b) generalization_claimed == 'population_claim' while evidence_scope reads single-subject
        (n=1 / one household / ...).
    """
    if not isinstance(scope, dict):
        return None
    claim_scope = scope.get("claim_scope") or ""
    evidence_scope = scope.get("evidence_scope") or ""
    generalization = scope.get("generalization_claimed")

    if _BROADENING_MARKERS.search(claim_scope) and not _BROADENING_MARKERS.search(evidence_scope):
        return (
            "rule6(scope): claim_scope names a broader-population marker "
            f"not present in evidence_scope (claim_scope={claim_scope!r}, evidence_scope={evidence_scope!r})"
        )
    if generalization == "population_claim" and _SINGLE_SUBJECT_MARKERS.search(evidence_scope):
        return (
            "rule6(scope): generalization_claimed is 'population_claim' but evidence_scope reads "
            f"single-subject (evidence_scope={evidence_scope!r})"
        )
    return None


def _parse_date(value):
    if not value or not isinstance(value, str):
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def _bounded_exception_90day_error(independent_check):
    """Rules 4/9's bounded I2+I4 exception (chair ruling B4, §4.2): `expires_at` must be within
    90 days of `date`. Date-diff arithmetic is explicitly named kernel-only (schema/README.md).
    Returns an error string, or None when the check does not apply or passes.
    """
    if not isinstance(independent_check, dict):
        return None
    expires_at = independent_check.get("expires_at")
    start = independent_check.get("date")
    if not expires_at:
        return None  # nothing to check; presence-only is schema's job
    d0 = _parse_date(start)
    d1 = _parse_date(expires_at)
    if d0 is None or d1 is None:
        return "bounded-exception: date/expires_at present but not parseable as YYYY-MM-DD"
    delta_days = (d1 - d0).days
    if delta_days < 0:
        return f"bounded-exception: expires_at ({expires_at}) is before date ({start})"
    if delta_days > 90:
        return f"bounded-exception: expires_at is {delta_days} days after date -- exceeds the 90-day ceiling (chair ruling B4)"
    return None


def _uses_bounded_exception(card):
    disclaimers = card.get("disclaimers_emitted") or []
    has_same_vendor = any((d or {}).get("id") == "D-SAME-VENDOR" for d in disclaimers)
    ic = card.get("independent_check") or {}
    return has_same_vendor and bool(ic.get("expires_at"))


# --------------------------------------------------------------------------------------------
# MUST-6: kernel gate rule 12 (D-LENS-UNSIGNED) + D-LENS-UNCITED.
# FOUNDATION_v0.5.md:593-600 specifies rule 12 as a hard validation error with zero prior code,
# schema, or test presence anywhere (reviews/ARCH_integrity.md F2). Implemented here as two
# kernel-only checks, narrower than FOUNDATION's own always-non-empty-signature text (task scope:
# "if lens_used or lens_ref is present and hypothesis_world.signature is empty") -- a card that
# never names a lens is untouched by either rule.
# --------------------------------------------------------------------------------------------

def _lens_unsigned_error(card):
    """Kernel rule 12 (D-LENS-UNSIGNED, §3.3 rule 12): when `lens_translation.lens_ref` is
    non-empty, `hypothesis_world.signature` must be non-empty AND must actually name the lens
    `lens_ref` points at (FOUNDATION_v0.5.md:593-600, "a hard validation error, not a warning").
    Returns an error string, or None when no lens is used or the signature is present and names
    it. The "names the lens" half is a text-containment heuristic (tagged `HEURISTIC:`, same
    convention as rule 6/rule 8 above) -- the kernel checks structure, not whether the prose is
    actually true.
    """
    lens = card.get("lens_translation") or {}
    lens_ref = lens.get("lens_ref")
    if not lens_ref:
        return None
    hw = card.get("hypothesis_world") or {}
    signature = hw.get("signature")
    if not (isinstance(signature, str) and signature.strip()):
        return (
            f"rule12(D-LENS-UNSIGNED): lens_translation.lens_ref={lens_ref!r} is set but "
            "hypothesis_world.signature is empty/absent -- a hard validation error (§3.3 rule "
            "12), not a warning."
        )
    if lens_ref not in signature:
        return (
            "HEURISTIC: rule12(D-LENS-UNSIGNED): hypothesis_world.signature is present but does "
            f"not name the lens lens_ref points at ({lens_ref!r} not found in the signature "
            "text) -- §3.3 rule 12 requires the signature to actually name the lens."
        )
    return None


def _lens_uncited_error(card, citation_cards):
    """D-LENS-UNCITED (§7.4 lens-citation gate, FOUNDATION_v0.5.md:780): when
    `lens_translation.lens_ref` is set, a `citation_card` with `status: VERIFIED` matching that
    lens must exist. `validate_claim_card`'s own signature does not otherwise receive
    citation_card payloads (the same documented gap `gate_release`'s own docstring already
    discloses for citation VERIFIED reachability generally) -- this function is only evaluable
    when the caller explicitly supplies `citation_cards`. Match rule: a citation_card counts as
    citing the lens when its `id` or `identifier.value` equals `lens_ref` exactly (a structural
    cross-reference, not a semantic check that the citation is actually about that lens).

    Returns an error string, None (rule does not apply / is satisfied), or the sentinel
    `"__NOT_CHECKED__"` when `lens_ref` is set but `citation_cards` was not supplied -- callers
    should surface that sentinel as a warning, never silently treat it as a pass.
    """
    lens = card.get("lens_translation") or {}
    lens_ref = lens.get("lens_ref")
    if not lens_ref:
        return None
    if citation_cards is None:
        return "__NOT_CHECKED__"
    matches = [
        c for c in citation_cards
        if isinstance(c, dict) and (
            c.get("id") == lens_ref or (c.get("identifier") or {}).get("value") == lens_ref
        )
    ]
    verified = [c for c in matches if c.get("status") == "VERIFIED"]
    if not verified:
        return (
            f"rule12b(D-LENS-UNCITED): lens_translation.lens_ref={lens_ref!r} is set but no "
            "citation_card with status VERIFIED matching that ref was found among the supplied "
            "citation_cards (§7.4 lens-citation gate) -- hard release-gate block, not a soft "
            "disclaimer-and-proceed."
        )
    return None


# --------------------------------------------------------------------------------------------
# Kernel rule 15 / rule16w: responsibility per Data->Inference->Claim arrow, empirical_extension
# (founder instruction 2026-09-04, BBL-2026-09-04-083/084; FOUNDATION_v0.5.md §2.1b).
# NOTE: numbered 15/16 so as not to collide with FOUNDATION §3.3 rules 13-14 (channel / CHALLENGES); this is a kernel check keyed to the `responsibility` block, distinct
# from FOUNDATION_v0.5.md §3.3's own pre-existing (unimplemented, spec-only) rule 13/14 text about
# `evidence_relations[].channel` (Bridge Burden) and `bearing: CHALLENGES` -- both numbers were
# already taken in the spec text before this pass. Flagged here rather than silently renumbered,
# per one-fact-one-home discipline; a future pass should reconcile the two rule-13/14 numberings.
# --------------------------------------------------------------------------------------------

def _responsibility_error_for_card(card):
    """Kernel rule 15: when `responsibility` is present, `inference_to_claim` must be exactly
    "human" -- the human signs the claim; AI is never an author (FOUNDATION_v0.5.md §2.1b,
    AGENTS.md gate rule 5). Returns an error string, or None when the field is absent or valid.
    """
    responsibility = card.get("responsibility")
    if responsibility is None:
        return None
    if not isinstance(responsibility, dict):
        return None
    if responsibility.get("inference_to_claim") != "human":
        return "rule15: Inference→Claim must be signed by the human"
    ownership = responsibility.get("ownership")
    if isinstance(ownership, dict):
        bad = [k for k in ("problem", "question", "hypothesis_selection") if ownership.get(k) != "human"]
        if bad:
            return "rule15: ownership of %s must stay human (FOUNDATION §2.1c, BBL-2026-09-04-086/088)" % ", ".join(bad)
    return None


def _responsibility_warning_for_card(card):
    """Kernel rule 15 (warning half): when `responsibility` is absent entirely, warn rather than
    fail -- the block is optional (K0-stub authoring-cost floor, §3.2a), but silence about who
    performed each spine arrow is named, not swallowed.
    """
    if card.get("responsibility") is None:
        return "rule15w: responsibility per arrow not declared (Data→Inference→Claim)"
    return None


def _empirical_extension_warning_for_card(card):
    """Kernel rule 16 (warning): a claim_type EMPIRICAL card with no `empirical_extension` block
    (operationalization / study_design / bias_register / robustness) is legal but under-specified
    -- warn, never hard-fail (FOUNDATION_v0.5.md §2, founder instruction 2026-09-04).
    """
    if card.get("claim_type") == "EMPIRICAL" and card.get("empirical_extension") is None:
        return "rule16w: empirical claim without operationalization/study_design/bias_register/robustness"
    return None


# --------------------------------------------------------------------------------------------
# validate_claim_card
# --------------------------------------------------------------------------------------------

def validate_claim_card(card, allow_no_jsonschema=False, citation_cards=None):
    """Validate a claim_card payload against schema/claim_card.schema.json PLUS the kernel-only
    halves of FOUNDATION_v0.5.md §3.3's 12 rules (5, 6, 8, 12, the bounded-exception date
    arithmetic inside 4/9, and the MUST-7 MC-01 human-Approver-identity extension), plus the
    kernel rule 15 (responsibility.inference_to_claim must be "human" -- hard error -- and a
    warning `rule15w` when `responsibility` is absent) and rule16w (warning when claim_type is
    EMPIRICAL but `empirical_extension` is absent). Returns a Result.

    Schema-enforced rules (1, 2, 3-presence, 4-plain, 7-approximated, 9-plain, 10, 11, and the
    D-INDEPENDENCE disclaimer-trigger worked example) are checked by the schema itself when
    jsonschema is importable; this function does not re-implement them by hand (one-fact-one-
    home: the rule's SHAPE lives in claim_card.schema.json's `allOf`, not duplicated here).

    `allow_no_jsonschema` (MUST-4): see `_schema_validate_gated`'s docstring -- default False
    fails closed the moment the real schema validator could not run; pass True only when the
    caller has a real reason to accept the coarse fallback check, which downgrades the returned
    tier to `Dr`.

    `citation_cards` (MUST-6, D-LENS-UNCITED): optional list of citation_card payloads, used only
    to check the lens-citation gate when `lens_translation.lens_ref` is set. Omitting it (the
    default) does not fabricate a pass -- see `_lens_uncited_error`'s docstring; the gap is
    surfaced as a warning instead.
    """
    if not isinstance(card, dict):
        return _result(ok=False, errors=["validate_claim_card: instance is not an object"])

    errors, warnings, tier, _used_fallback = _schema_validate_gated(
        card, "claim_card.schema.json", allow_no_jsonschema
    )

    # Kernel-only rule 5 (MC-01)
    errors.extend(_mc01_errors_for_card(card))

    # Kernel-only rule 6 (scope containment)
    scope_err = _scope_exceeds_evidence(card.get("scope"))
    if scope_err:
        errors.append(scope_err)

    # Kernel-only rule 8 (EXTERNAL_VALIDATION_PROPOSED text scan) -- hard fail
    hits = _scan_for_external_validation_proposed(card)
    for path, matched in hits:
        errors.append(
            f"HEURISTIC: rule8(EXTERNAL_VALIDATION_PROPOSED): '{matched}' at {path} proposes "
            "external/institutional validation as a legitimacy lever (EPIS-KNOWLEDGE-VALIDATION forbids this)"
        )

    # Kernel-only date arithmetic for the bounded I2+I4 exception (rules 4 & 9)
    if _uses_bounded_exception(card):
        exc_err = _bounded_exception_90day_error(card.get("independent_check"))
        if exc_err:
            errors.append(f"rule4/9(bounded-exception): {exc_err}")

    # MUST-7: MC-01 human-Approver-identity extension
    human_err = _human_approver_error_for_card(card)
    if human_err:
        errors.append(human_err)

    # Kernel rule 12 (D-LENS-UNSIGNED)
    lens_err = _lens_unsigned_error(card)
    if lens_err:
        errors.append(lens_err)

    # D-LENS-UNCITED -- only evaluable when citation_cards was supplied (see docstring above)
    uncited_err = _lens_uncited_error(card, citation_cards)
    if uncited_err == "__NOT_CHECKED__":
        warnings.append(
            "D-LENS-UNCITED not checked -- validate_claim_card was not given citation_cards "
            "(lens_translation.lens_ref is set); pass citation_cards=[...] to close this gap."
        )
    elif uncited_err:
        errors.append(uncited_err)

    # Kernel rule 15 (responsibility per Data->Inference->Claim arrow)
    resp_err = _responsibility_error_for_card(card)
    if resp_err:
        errors.append(resp_err)
    else:
        resp_warn = _responsibility_warning_for_card(card)
        if resp_warn:
            warnings.append(resp_warn)

    # Kernel rule 16 (warning): EMPIRICAL claim without empirical_extension
    emp_warn = _empirical_extension_warning_for_card(card)
    if emp_warn:
        warnings.append(emp_warn)

    return _result(ok=not errors, errors=errors, warnings=warnings, tier=tier)


# --------------------------------------------------------------------------------------------
# validate_review_report / validate_citation_card / validate_release_manifest / validate_blackbox_note
# --------------------------------------------------------------------------------------------

def validate_review_report(report, maker_id=None, approver_id=None, allow_no_jsonschema=False):
    """Validate a review_report payload (§4.3, §7.3 Bounded-Judge Law). Returns a Result.

    `maker_id`/`approver_id` are OPTIONAL kernel-only cross-checks (schema/README.md: MC-01's
    "twin for review_report" -- reviewer_identity must differ from the artifact's own maker and
    approver, a check no single-document schema can express).

    `allow_no_jsonschema` (MUST-4): see `_schema_validate_gated`'s docstring.
    """
    if not isinstance(report, dict):
        return _result(ok=False, errors=["validate_review_report: instance is not an object"])

    errors, warnings, tier, _used_fallback = _schema_validate_gated(
        report, "review_report.schema.json", allow_no_jsonschema
    )

    if not report.get("verdict_tier"):
        errors.append("Bounded-Judge Law (§7.3): review_report has no verdict_tier -- an untiered verdict is invalid.")

    reviewer = report.get("reviewer_identity")
    if maker_id and reviewer and reviewer == maker_id:
        errors.append("MC-01(review_report): reviewer_identity == maker_id -- same-model/same-person self-review has no standing.")
    if approver_id and reviewer and reviewer == approver_id:
        errors.append("MC-01(review_report): reviewer_identity == approver_id -- the Approver's sign-off never substitutes for an independent check.")

    # MUST-7: MC-01 human-Approver-identity extension (mc_level L5 / independence_class I5)
    human_err = _human_approver_error_for_review(report)
    if human_err:
        errors.append(human_err)

    return _result(ok=not errors, errors=errors, warnings=warnings, tier=tier)


def _citation_source_first_errors(c):
    """Kernel rule 17 — source-first citation (founder ruling 2026-09-04, BBL-2026-09-04-100/101):
    a citation is written FROM the opened source, never from memory. When fetch_status is FETCHED
    (or PAYWALLED_ABSTRACT_ONLY) the card must carry the link it was read from, a page/section
    locator, a line/paragraph pointer and a verbatim exact_passage; a card lacking any of these
    may not stand above CANDIDATE. Returns a list of error strings."""
    errs = []
    fs = c.get("fetch_status")
    if fs in ("FETCHED", "PAYWALLED_ABSTRACT_ONLY"):
        missing = [k for k in ("fetched_from_url", "page_or_locator", "line_or_paragraph", "exact_passage") if not str(c.get(k) or "").strip()]
        if missing and c.get("status") not in (None, "CANDIDATE"):
            errs.append("rule17(source-first citation): status %s requires %s taken from the opened source (never from memory)" % (c.get("status"), ", ".join(missing)))
        elif missing:
            errs.append("rule17w(source-first citation): missing %s -- fill from the opened source before the card can leave CANDIDATE" % ", ".join(missing))
    return errs


def validate_citation_card(citation, allow_no_jsonschema=False):
    """Validate a citation_card payload (§7.8 Citation Integrity subsystem). Returns a Result.

    The two Integrity Firewall booleans (`metadata_verified` != `claim_match_verified`, NC-18)
    and the VERIFIED-requires-both-booleans / exact_passage-requires-claim_match_verified rules
    are schema-enforced (citation_card.schema.json's allOf); this function adds the one kernel-
    only cross-check the schema cannot express standalone: a SCRAMMED card must carry a non-null
    `xenon_ledger_ref` (the Xenon Ledger, §7.8, is append-only and every SCRAMMED card must be
    findable there -- a structural completeness check on the card's own two fields, not a claim
    about whether the ledger row actually exists on disk; see `xenon_ledger_check` below for the
    MUST-12 count/threshold half of this gate, run separately over a batch of citation_cards).

    `allow_no_jsonschema` (MUST-4): see `_schema_validate_gated`'s docstring.
    """
    if not isinstance(citation, dict):
        return _result(ok=False, errors=["validate_citation_card: instance is not an object"])

    errors, warnings, tier, _used_fallback = _schema_validate_gated(
        citation, "citation_card.schema.json", allow_no_jsonschema
    )

    if citation.get("status") == "SCRAMMED" and not citation.get("xenon_ledger_ref"):
        errors.append("citation_card: status SCRAMMED requires a non-null xenon_ledger_ref (§7.8 Xenon Ledger).")

    # Kernel rule 17 — source-first citation (founder ruling 2026-09-04, BBL-2026-09-04-100/101)
    r17 = _citation_source_first_errors(citation)
    errors.extend(e for e in r17 if e.startswith("rule17("))
    warnings.extend(e for e in r17 if e.startswith("rule17w"))

    return _result(ok=not errors, errors=errors, warnings=warnings, tier=tier)


def validate_release_manifest(manifest, allow_no_jsonschema=False):
    """Validate a release_manifest payload (§7.4 release state machine + PUB-ADVERSARIAL-REVIEW's
    seven dimensions R1-R7). Returns a Result.

    The Blackbox Note appendix precondition on Approved-for-Live, and gate_verdict FAIL never
    coexisting with an Approved-* status, are schema-enforced; this function adds the kernel-only
    check that no single R1-R7 dimension may read FAIL while the manifest's own `gate_verdict` is
    PASS (a cross-field consistency check the schema's allOf does not reach across all seven
    dimension sub-objects at once), plus the MUST-7 MC-01 human-Approver-identity extension.

    `allow_no_jsonschema` (MUST-4): see `_schema_validate_gated`'s docstring.
    """
    if not isinstance(manifest, dict):
        return _result(ok=False, errors=["validate_release_manifest: instance is not an object"])

    errors, warnings, tier, _used_fallback = _schema_validate_gated(
        manifest, "release_manifest.schema.json", allow_no_jsonschema
    )

    review = manifest.get("adversarial_review") or {}
    failed_dims = [
        k for k in (
            "r1_leak_scan", "r2_license_coverage", "r3_tier_fidelity", "r4_citation_accuracy",
            "r5_anchor_preservation_audit", "r6_overclaim_register_scan", "r7_completeness",
        )
        if isinstance(review.get(k), dict) and review[k].get("result") == "FAIL"
    ]
    if failed_dims and manifest.get("gate_verdict") == "PASS":
        errors.append(
            "release_manifest: gate_verdict is PASS but the following adversarial_review "
            f"dimension(s) read FAIL: {failed_dims} -- PUB-ADVERSARIAL-REVIEW (§7.4) forbids this."
        )

    if manifest.get("status") in ("Approved-for-Test", "Approved-for-Live") and not manifest.get(
        "blackbox_note_appendix_present"
    ):
        errors.append(
            "release_manifest: status advanced past Draft/Pending Review without "
            "blackbox_note_appendix_present -- hard precondition on every genre's Publish node (§6.4)."
        )

    # MUST-7: MC-01 human-Approver-identity extension
    human_err = _human_approver_error_for_manifest(manifest)
    if human_err:
        errors.append(human_err)

    return _result(ok=not errors, errors=errors, warnings=warnings, tier=tier)


def validate_blackbox_note(note, allow_no_jsonschema=False):
    """Validate a blackbox_note payload (§2.3/§2.4, chair ruling A1). Returns a Result.

    Raw verbatim human lines, never edited in place; the cooking log is append-only. The
    privacy_scan-before-any-public-line gate is schema-enforced; this function adds one kernel-
    only referential-integrity check the schema cannot express: every `cooking[].input_lines`
    entry must name a line number that actually exists in `lines[].n` (one-fact-one-home applied
    to the note's own internal cross-references).

    `allow_no_jsonschema` (MUST-4): see `_schema_validate_gated`'s docstring.
    """
    if not isinstance(note, dict):
        return _result(ok=False, errors=["validate_blackbox_note: instance is not an object"])

    errors, warnings, tier, _used_fallback = _schema_validate_gated(
        note, "blackbox_note.schema.json", allow_no_jsonschema
    )

    line_numbers = {ln.get("n") for ln in (note.get("lines") or []) if isinstance(ln, dict)}
    for i, cook in enumerate(note.get("cooking") or []):
        for n in (cook or {}).get("input_lines") or []:
            if n not in line_numbers:
                errors.append(f"blackbox_note: cooking[{i}].input_lines references line {n}, which does not exist in lines[].n")

    return _result(ok=not errors, errors=errors, warnings=warnings, tier=tier)


# --------------------------------------------------------------------------------------------
# compute_disclaimers
# --------------------------------------------------------------------------------------------

# Embedded minimal fallback table -- used ONLY when methodology/data/disclaimer_catalogue.json
# cannot be read. A small subset of the full 39-row catalogue (37 + D-LENS-UNSIGNED/D-LENS-UNCITED,
# MUST-6): exactly the ids this function can
# compute from a claim_card alone (see docstring below for the ones that need OTHER artifacts and
# are therefore out of scope for compute_disclaimers(card)).
_EMBEDDED_MINIMAL_DISCLAIMER_TABLE = [
    {"id": "D-STANDPOINT", "trigger": "ALWAYS", "params": []},
    {"id": "D-NONEXPERT", "trigger": "ALWAYS", "params": []},
    {"id": "D-NONCLAIM", "trigger": "ALWAYS", "params": []},
    {"id": "D-TIER", "trigger": "ALWAYS", "params": ["tier"]},
    {"id": "D-K-STATE", "trigger": "ALWAYS", "params": ["k_state"]},
    {"id": "D-AUTHORSHIP", "trigger": "ALWAYS", "params": []},
    {"id": "D-REVISION-LIVE", "trigger": "ALWAYS", "params": []},
    {"id": "D-NO-EPISTEMIC-VETO", "trigger": "ALWAYS", "params": []},
    {"id": "D-BLACKBOX-NOTE", "trigger": "ALWAYS", "params": ["origin_blackbox_ref"]},
    {"id": "D-SCOPE", "trigger": "scope.generalization_claimed != none", "params": ["generalization_claimed"]},
    {"id": "D-AIFILL", "trigger": "any ai_filled.* used", "params": ["field_name"]},
    {"id": "D-INDEPENDENCE", "trigger": "max(tested.evidence_relations[].independence_class) in {I0,I1,I2}", "params": []},
    {"id": "D-CANDIDATE-STATUS", "trigger": "independent_check.independence_class not in {I4,I5}", "params": []},
    {"id": "D-TRANSLATION", "trigger": "translation present or thai_tci or companion_of", "params": ["translation_status"]},
    {"id": "D-DISSENT-PRESERVED", "trigger": "len(dissent_records) > 0", "params": []},
    {"id": "D-SILENT-LIFT-GUARD", "trigger": "flags non-empty or an unidentified assumption", "params": ["flag_ids"]},
    {"id": "D-EXTERNAL-INPUT", "trigger": "len(ledger.borrowed) > 0", "params": ["source_ref"]},
    {"id": "D-DERIVED-PATTERNS", "trigger": "ledger.borrowed references a private ANSE.ASIA repo", "params": ["private_repo_name"]},
    {"id": "D-LEGAL-NEQ-EPISTEMIC", "trigger": "legal_epistemic_separation.applicable == true", "params": []},
    {"id": "D-NOT-DIAGNOSTIC", "trigger": "HEURISTIC domain scan (health/clinical/legal/financial)", "params": []},
    {"id": "D-NO-VERTICAL-AUTHORITY", "trigger": "HEURISTIC text scan (peer review/venue/institutional accept/...)", "params": []},
    {"id": "D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE", "trigger": "declared_basis is lived experience and generalization_claimed != none", "params": []},
]

def _load_private_source_names():
    """Names of private source repositories are NOT shipped in this public kernel. They are read
    from the git-ignored file registry/private_source_names.txt (one name per line) or the
    GLOSA_PRIVATE_SOURCE_NAMES env var (comma-separated); default empty list."""
    import os as _os
    names = [n.strip() for n in _os.environ.get("GLOSA_PRIVATE_SOURCE_NAMES", "").split(",") if n.strip()]
    f = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "registry", "private_source_names.txt")
    if _os.path.exists(f):
        names += [l.strip() for l in open(f, encoding="utf-8") if l.strip() and not l.startswith("#")]
    return names


_PRIVATE_REPO_NAMES = _load_private_source_names()

_DOMAIN_SAFETY_KEYWORDS = re.compile(
    r"\b(diagnos|clinical|treatment|medication|symptom|legal advice|lawsuit|financial advice|investment advice)\w*\b",
    re.IGNORECASE,
)
_VERTICAL_AUTHORITY_KEYWORDS = re.compile(
    r"\b(peer review(ed)?|publication venue|institutional accept|journal prestige|impact factor)\b",
    re.IGNORECASE,
)
_DVP_NOT_K2_KEYWORDS = re.compile(r"\b(verified|peer reviewed|certified|K2|K3)\b", re.IGNORECASE)

_INDEPENDENCE_ORDER = ["I0", "I1", "I2", "I3", "I4", "I5"]


def _max_independence_class(evidence_relations):
    classes = [er.get("independence_class") for er in (evidence_relations or []) if isinstance(er, dict)]
    classes = [c for c in classes if c in _INDEPENDENCE_ORDER]
    if not classes:
        return None
    return max(classes, key=_INDEPENDENCE_ORDER.index)


def _load_disclaimer_catalogue():
    """Return (rows, source_str). Reads methodology/data/disclaimer_catalogue.json when present
    (per FOUNDATION §5's canonical home); falls back to the embedded minimal table otherwise.
    `rows` is always a list of {id, trigger, params} dicts (the full catalogue file's extra
    fields -- category/wording_th/wording_en/placement/mandatory -- are not needed by
    compute_disclaimers and are left untouched, one-fact-one-home: this function reads, never
    redefines, the catalogue).
    """
    if DISCLAIMER_CATALOGUE_PATH.is_file():
        try:
            data = json.loads(DISCLAIMER_CATALOGUE_PATH.read_text(encoding="utf-8"))
            rows = data.get("disclaimers", [])
            if rows:
                return rows, str(DISCLAIMER_CATALOGUE_PATH)
        except (OSError, ValueError):
            pass
    return _EMBEDDED_MINIMAL_DISCLAIMER_TABLE, "EMBEDDED_MINIMAL_DISCLAIMER_TABLE (methodology/data/disclaimer_catalogue.json not found/unreadable)"


_KNOWN_DISCLAIMER_IDS_NOT_COMPUTABLE_FROM_CARD_ALONE = {
    # These triggers reference artifacts compute_disclaimers(card) does not receive (a
    # route_dependence_matrix, a disagreement_ledger, a search_log, a conversion_plan, a
    # neighbour_table, or another public surface's own wording) -- listed here so the function's
    # silence about them is a documented decision, not an accidental omission.
    "D-INDEPENDENCE-LEVEL", "D-DVP-NOT-K2", "D-SAME-VENDOR", "D-OPERATOR-SHARED",
    "D-DISAGREEMENT-OPEN", "D-NO-NEGATIVE-UNVERIFIED-PERSON", "D-PARTIAL-SET",
    "D-COMPARISON", "D-CITATION-UNVERIFIED", "D-ADVISOR", "D-ADVISOR-NOT-K2",
    "D-ADVISOR-EXPIRED", "D-LIT-MODE", "D-LIT-NOT-OBTAINED", "D-LIT-CONCENTRATED",
}


def compute_disclaimers(card, citation_cards=None):
    """Compute the subset of FOUNDATION_v0.5.md §5's disclaimer catalogue whose trigger is fully
    evaluable from a claim_card object alone. Returns a list of {"id": ..., "params": {...}}
    dicts (matching `disclaimers_emitted`'s own shape, common.defs.json#/definitions/disclaimer_ref).

    Reads `methodology/data/disclaimer_catalogue.json` when present (see `_load_disclaimer_catalogue`
    for exactly which id set that resolves to); otherwise falls back to the embedded minimal
    table `_EMBEDDED_MINIMAL_DISCLAIMER_TABLE` above -- this function always tells you which one
    it used via the returned list's own `_source` marker at index 0 having been considered (see
    `source` in the tuple this delegates to; exposed separately so the return type stays a plain
    list, matching the task's `compute_disclaimers(card)->[ids with params]` signature).

    `citation_cards` (MUST-6, D-LENS-UNCITED, optional): same convention as
    `validate_claim_card`'s own parameter of the same name -- only used to evaluate D-LENS-UNCITED
    when `lens_translation.lens_ref` is set; omitted, that one id is simply not emitted (an honest
    silence, not a false negative claim that the gate was checked and passed).

    NOT computed here (need an artifact beyond the card -- see
    `_KNOWN_DISCLAIMER_IDS_NOT_COMPUTABLE_FROM_CARD_ALONE`): D-INDEPENDENCE-LEVEL, D-SAME-VENDOR,
    D-OPERATOR-SHARED, D-DISAGREEMENT-OPEN, D-NO-NEGATIVE-UNVERIFIED-PERSON, D-PARTIAL-SET,
    D-COMPARISON, D-CITATION-UNVERIFIED, D-ADVISOR*, D-LIT-*. `D-DVP-NOT-K2` IS attempted here as
    a best-effort text scan (see below) even though its full trigger also needs a public-surface
    text outside the card; when the card itself contains no such surface text it simply will not
    fire, which is honest (never a false positive), not a full implementation of the row.
    """
    catalogue_rows, _source = _load_disclaimer_catalogue()
    known_ids = {row["id"] for row in catalogue_rows if isinstance(row, dict) and "id" in row}

    out = []

    def emit(disc_id, params=None):
        if known_ids and disc_id not in known_ids:
            return  # never emit an id the loaded catalogue does not itself define
        entry = {"id": disc_id}
        if params:
            entry["params"] = params
        out.append(entry)

    # ALWAYS-on rows
    emit("D-STANDPOINT")
    emit("D-NONEXPERT")
    emit("D-NONCLAIM")
    emit("D-AUTHORSHIP")
    emit("D-REVISION-LIVE")
    emit("D-NO-EPISTEMIC-VETO")
    if card.get("tier"):
        emit("D-TIER", {"tier": card.get("tier")})
    if card.get("k_state"):
        emit("D-K-STATE", {"k_state": card.get("k_state")})
    if card.get("origin_blackbox_ref"):
        emit("D-BLACKBOX-NOTE", {"origin_blackbox_ref": card.get("origin_blackbox_ref")})

    # D-SCOPE
    scope = card.get("scope") or {}
    if scope.get("generalization_claimed") not in (None, "none"):
        emit("D-SCOPE", {"n": scope.get("evidence_scope"), "generalization_claimed": scope.get("generalization_claimed")})

    # D-AIFILL
    ai_filled = (card.get("five_questions") or {}).get("ai_filled") or {}
    if card.get("shape") == "stub":
        if ai_filled.get("used"):
            emit("D-AIFILL", {"field_name": "used"})
    else:
        used_fields = [k for k, v in ai_filled.items() if isinstance(v, str) and v.strip() and v.strip().lower() != "none identified"]
        if used_fields:
            emit("D-AIFILL", {"field_name": used_fields})

    # D-INDEPENDENCE
    evidence_relations = (card.get("five_questions") or {}).get("tested", {}).get("evidence_relations") or []
    max_ic = _max_independence_class(evidence_relations)
    if max_ic in ("I0", "I1", "I2"):
        emit("D-INDEPENDENCE")

    # D-DVP-NOT-K2 (best-effort; needs the card's own text plus max_ic < I5)
    if max_ic != "I5":
        text_fields = [
            (card.get("statement") or {}).get("text"),
            ((card.get("statement") or {}).get("translation") or {}).get("text"),
        ]
        if any(t and _DVP_NOT_K2_KEYWORDS.search(t) for t in text_fields):
            emit("D-DVP-NOT-K2")

    # D-CANDIDATE-STATUS
    ic_class = (card.get("independent_check") or {}).get("independence_class")
    if ic_class not in ("I4", "I5"):
        emit("D-CANDIDATE-STATUS")

    # D-TRANSLATION
    has_translation = bool((card.get("statement") or {}).get("translation"))
    if has_translation or card.get("venue_track") == "thai_tci" or card.get("companion_of"):
        emit("D-TRANSLATION", {"translation_status": ((card.get("statement") or {}).get("translation") or {}).get("translation_status")})

    # D-DISSENT-PRESERVED
    dissent = (card.get("five_questions") or {}).get("tested", {}).get("dissent_records") or []
    if dissent:
        emit("D-DISSENT-PRESERVED")

    # D-SILENT-LIFT-GUARD
    slc_flags = (card.get("silent_lift_check") or {}).get("flags") or []
    unidentified = [a for a in (card.get("five_questions") or {}).get("assumed") or [] if (a or {}).get("identification_level") == "unidentified"]
    if slc_flags or unidentified:
        emit("D-SILENT-LIFT-GUARD", {"flag_ids": slc_flags})

    # D-EXTERNAL-INPUT / D-DERIVED-PATTERNS
    borrowed = (card.get("ledger") or {}).get("borrowed") or []
    if borrowed:
        emit("D-EXTERNAL-INPUT", {"source_ref": borrowed})
        hit_repos = [name for name in _PRIVATE_REPO_NAMES if any(name in str(b) for b in borrowed)]
        if hit_repos:
            emit("D-DERIVED-PATTERNS", {"private_repo_name": hit_repos})

    # D-LEGAL-NEQ-EPISTEMIC
    if (card.get("legal_epistemic_separation") or {}).get("applicable"):
        emit("D-LEGAL-NEQ-EPISTEMIC")

    # D-NOT-DIAGNOSTIC (HEURISTIC)
    domain_text = " ".join(
        str(x) for x in [
            (card.get("statement") or {}).get("text"),
            (card.get("standpoint") or {}).get("declared_basis"),
        ] if x
    )
    if _DOMAIN_SAFETY_KEYWORDS.search(domain_text):
        emit("D-NOT-DIAGNOSTIC")

    # D-NO-VERTICAL-AUTHORITY (HEURISTIC)
    if _VERTICAL_AUTHORITY_KEYWORDS.search(domain_text):
        emit("D-NO-VERTICAL-AUTHORITY")

    # D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE
    declared_basis = str((card.get("standpoint") or {}).get("declared_basis") or "")
    if re.search(r"lived experience|practice.?lived", declared_basis, re.IGNORECASE) and scope.get("generalization_claimed") not in (None, "none"):
        emit("D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE")

    # D-LENS-UNSIGNED (kernel rule 12, MUST-6)
    if _lens_unsigned_error(card):
        emit("D-LENS-UNSIGNED", {"lens_ref": (card.get("lens_translation") or {}).get("lens_ref")})

    # D-LENS-UNCITED (§7.4 lens-citation gate, MUST-6) -- only evaluable when citation_cards given
    uncited = _lens_uncited_error(card, citation_cards)
    if uncited and uncited != "__NOT_CHECKED__":
        emit("D-LENS-UNCITED", {"lens_ref": (card.get("lens_translation") or {}).get("lens_ref")})

    return out


# --------------------------------------------------------------------------------------------
# route_genre
# --------------------------------------------------------------------------------------------

def route_genre(card, context=None):
    """FOUNDATION_v0.5.md §6.3b's 9-question genre routing procedure, read directly off a claim
    card's own fields wherever the procedure names one. Returns
    {"genre": <id-or-None>, "venue_track": ..., "companion_of": ..., "reasons": [str, ...]}.

    Steps 1-7 are evaluated IN ORDER and the procedure returns on the FIRST "yes" (§6.3b's own
    literal text: "yes -> **genre**. No -> continue"), so a card that would satisfy a later,
    weaker/default-ish branch (step 7's practice/case-study catch-most) never gets there once an
    earlier, more specific branch already matched. Step 8 (`conceptual`) is the terminal fallback
    when nothing above matched. Step 9 (`MIXED_GENRE`) is NOT auto-triggered by ordinary
    sequential routing (which by construction only ever returns one id) -- it is an explicit,
    opt-in second pass: pass `context={"check_mixed_genre": True}` to also evaluate every step's
    condition independently (ignoring the short-circuit) and return `MIXED_GENRE` if more than
    one is true, naming every matched id in `reasons` for the human Approver's tie-break (Human
    Mastery Gate, §7.5) -- this matches §6.3b's own framing that detecting "comparable strength"
    across branches is the case a human resolves, not something the ordinary sequential procedure
    computes as a side effect.

    `context` is an OPTIONAL dict for the handful of §6.3b questions that name an artifact the
    claim card itself does not carry (a `search_log`, an explicit "this replies to claim X"
    pointer, or a human's bounded-case call at step 7's second branch). Keys read, all optional:
      - has_search_log: bool          (step 2)
      - target_claim_ref: str         (step 4, in addition to reading lineage.derives_from directly)
      - bounded_case: bool            (step 7's inner branch: case_study vs empirical_qual_practice)
      - check_mixed_genre: bool       (opt in to the step-9 tie detector described above)

    `venue_track` and `companion_of` are read straight off the card and are NEVER inputs to the
    9-step procedure itself (§6.3b's own closing rule).
    """
    context = context or {}

    lens = card.get("lens_translation") or {}
    formal_applicability = lens.get("formal_applicability")
    evidence_relations = (card.get("five_questions") or {}).get("tested", {}).get("evidence_relations") or []
    no_mechanical_evidence = not any((er or {}).get("independence_class") in ("I4", "I5") for er in evidence_relations)

    seen = (card.get("five_questions") or {}).get("seen") or {}
    access_model = str(seen.get("access_model") or "")

    lineage = card.get("lineage") or {}
    derives_from = lineage.get("derives_from") or []

    claim_type = card.get("claim_type")
    assumed = (card.get("five_questions") or {}).get("assumed") or []
    has_decision_policy_artifact = any((a or {}).get("type") == "decision_policy_augmentation" for a in assumed)

    generalization = (card.get("scope") or {}).get("generalization_claimed")
    has_named_strength = any((er or {}).get("strength") for er in evidence_relations)

    declared_basis = str((card.get("standpoint") or {}).get("declared_basis") or "")
    method_basis = str((card.get("standpoint") or {}).get("method_basis") or "")
    combined_standpoint_text = declared_basis + " " + method_basis
    names_direct_practice = bool(re.search(r"\b(observation|practice|lived|household|direct)\b", combined_standpoint_text, re.IGNORECASE))
    is_bounded_case = context.get("bounded_case", True) is not False

    # Ordered (id, condition, reason) triples -- §6.3b steps 1-7, evaluated in this exact order.
    steps = [
        (
            "formal_proof",
            formal_applicability == "exact_functional" and no_mechanical_evidence,
            "step1: formal_applicability=exact_functional and no I4/I5 evidence_relation yet (a proof is intended, not yet mechanically checked)",
        ),
        (
            "systematic_review",
            bool(context.get("has_search_log")),
            "step2: context.has_search_log is True (a documented search_log exists for this claim)",
        ),
        (
            "archival",
            bool(seen.get("retrievable_original")) and bool(re.search(r"\b(record|register|archive|document)\b", access_model, re.IGNORECASE)),
            f"step3: seen.retrievable_original=True and seen.access_model names a retrievable archival record ({access_model!r})",
        ),
        (
            "position_reply",
            (not card.get("companion_of")) and bool(context.get("target_claim_ref") or len(derives_from) == 1),
            f"step4: companion_of is null and exactly one target is named (lineage.derives_from={derives_from!r} or context.target_claim_ref)",
        ),
        (
            "design_science",
            claim_type in ("DECISION", "FORMAL") and has_decision_policy_artifact,
            "step5: claim_type in {DECISION,FORMAL} and an assumed[] entry names decision_policy_augmentation (a built artifact)",
        ),
        (
            "empirical_quant",
            generalization == "population_claim" and bool(evidence_relations) and has_named_strength,
            "step6: scope.generalization_claimed=population_claim with a frozen/named evidence_relations set",
        ),
        (
            "case_study" if is_bounded_case else "empirical_qual_practice",
            generalization in ("none", "pattern_candidate") and names_direct_practice,
            "step7: bounded, individually-identifiable case named -> case_study" if is_bounded_case
            else "step7: a practice pattern without one bounded case -> empirical_qual_practice",
        ),
    ]

    reasons = []
    genre = None
    for step_id, cond, reason in steps:
        step_num = reason.split(":", 1)[0]
        if cond:
            genre = step_id
            reasons.append(f"{reason} -> {step_id}")
            break
        reasons.append(f"{step_num}: no -> continue")

    # Step 8 -- conceptual (terminal fallback; only reached if nothing above matched)
    if genre is None:
        if formal_applicability == "not_applicable_narrative":
            genre = "conceptual"
            reasons.append("step8: formal_applicability=not_applicable_narrative and no earlier branch matched -> conceptual")
        else:
            reasons.append("step8: no branch matched and formal_applicability != not_applicable_narrative -- a human Approver must set genre manually (§6.3b has no default for this case)")

    # Step 9 -- MIXED_GENRE, opt-in only (see docstring: sequential routing above never produces
    # this on its own; a caller must explicitly ask for the tie-detection pass).
    if context.get("check_mixed_genre"):
        all_matches = [step_id for step_id, cond, _ in steps if cond]
        if formal_applicability == "not_applicable_narrative" and "conceptual" not in all_matches and not any(cond for _, cond, _ in steps):
            all_matches.append("conceptual")
        unique = []
        for g in all_matches:
            if g not in unique:
                unique.append(g)
        if len(unique) > 1:
            genre = "MIXED_GENRE"
            reasons.append(
                f"step9: check_mixed_genre requested -- more than one branch matched independently ({unique}) -> "
                "MIXED_GENRE; a human Approver breaks the tie for the paper's primary structure (Human Mastery Gate, §7.5)"
            )

    return {
        "genre": genre,
        "venue_track": card.get("venue_track"),
        "companion_of": card.get("companion_of"),
        "reasons": reasons,
    }


# --------------------------------------------------------------------------------------------
# independence_ceiling
# --------------------------------------------------------------------------------------------

_TIER_CEILING_BY_INDEPENDENCE = {
    "I0": "Dr", "I1": "Dr", "I2": "Dr",
    "I3": "finite_diagnostic",
    "I4": "Th_coqc", "I5": "Th_coqc",
}
_K_STATE_CEILING_BY_INDEPENDENCE = {
    "I0": "K0", "I1": "K0", "I2": "K0",
    "I3": "K1", "I4": "K1",
    "I5": "K2",
}
_TIER_STRENGTH = {"Open": 0, "definition": 0, "Dr": 1, "fit_calibrated": 2, "finite_diagnostic": 3, "Th_coqc": 4}
_K_STATE_STRENGTH = {"K0": 0, "K1": 1, "K2": 2, "K3": 3}


def independence_ceiling(evidence_relations):
    """§4.2's "ordering rule": the maximum claim tier/k_state a route set can support is bounded
    by the HIGHEST independence level actually reached, never by the count of routes at a lower
    level (`ManyModels⇏Independence`, NC-31). Returns
    {"max_independence_class": ..., "max_tier": ..., "max_k_state": ...}.

    `max_tier`/`max_k_state` here are CEILINGS -- the most this evidence set could ever license
    per §4.2's table -- never a claim that the card in front of you actually carries that tier;
    `validate_claim_card`'s rules 2/3/4/9 are the actual gate, this function is descriptive.
    I5's true K3 ceiling additionally requires "a formal/empirical constraint" (§4.2) not
    reducible to independence_class alone, per FOUNDATION's own text -- this function returns the
    guaranteed K2 floor for I5 and leaves K3 to a human/other check, rather than over-claim it.
    """
    max_ic = _max_independence_class(evidence_relations)
    if max_ic is None:
        return {"max_independence_class": None, "max_tier": "Dr", "max_k_state": "K0"}
    return {
        "max_independence_class": max_ic,
        "max_tier": _TIER_CEILING_BY_INDEPENDENCE[max_ic],
        "max_k_state": _K_STATE_CEILING_BY_INDEPENDENCE[max_ic],
    }


# --------------------------------------------------------------------------------------------
# defeater_route
# --------------------------------------------------------------------------------------------

def defeater_route(provenance_dag, defeated_node):
    """Readout Condition Proposition 3: "paths not containing the node survive; lost iff no path
    survives." `provenance_dag` is `{"nodes": [{"id": ...}], "edges": [{"from": ..., "to": ...}]}`
    (claim_card.provenance_dag's own shape). Returns
    {"surviving_paths": [[node_id, ...], ...], "distinction_lost": bool, "all_paths_count": int,
    "cyclic": bool}.

    A "path" here is any root-to-leaf simple path through the DAG (a root = a node no edge points
    TO as a `to`; a leaf = a node no edge points FROM as a `from`) -- the set of complete
    provenance chains this graph actually represents. `distinction_lost` is True iff at least one
    path existed before removing `defeated_node` AND none of them survive its removal; a DAG with
    zero paths to begin with is reported as `distinction_lost: False, all_paths_count: 0` (there
    was nothing to lose -- the kernel never manufactures a loss that was not structurally there).
    """
    nodes = [(n or {}).get("id") for n in (provenance_dag or {}).get("nodes") or []]
    edges = [((e or {}).get("from"), (e or {}).get("to")) for e in (provenance_dag or {}).get("edges") or []]
    node_set = set(nodes)

    adjacency = {n: [] for n in nodes}
    has_incoming = {n: False for n in nodes}
    for f, t in edges:
        if f in node_set and t in node_set:
            adjacency.setdefault(f, []).append(t)
            has_incoming[t] = True

    roots = [n for n in nodes if not has_incoming.get(n, False)]
    leaves = [n for n in nodes if not adjacency.get(n)]

    all_paths = []
    cyclic = False

    def dfs(node, path, visited):
        nonlocal cyclic
        if node in visited:
            cyclic = True
            return
        path = path + [node]
        visited = visited | {node}
        children = adjacency.get(node, [])
        if not children:
            all_paths.append(path)
            return
        for c in children:
            dfs(c, path, visited)

    for r in roots:
        dfs(r, [], set())

    if not all_paths and nodes and not roots:
        # every node has incoming edges -> pure cycle, no roots at all
        cyclic = True

    surviving_paths = [p for p in all_paths if defeated_node not in p]
    distinction_lost = bool(all_paths) and not surviving_paths

    return {
        "surviving_paths": surviving_paths,
        "distinction_lost": distinction_lost,
        "all_paths_count": len(all_paths),
        "cyclic": cyclic,
    }


# --------------------------------------------------------------------------------------------
# silent_lift_check (top-level, standalone from validate_claim_card)
# --------------------------------------------------------------------------------------------

def silent_lift_check(card):
    """The mechanized test for the Readout Condition's E∧A∧D failure mode named in §3.1: a card
    that answers Q1/Q2/Q4 honestly but misattributes Q3 (crediting the source with a distinction
    AI actually supplied). Compares `silent_lift_check.represented_dependency_set` against
    `silent_lift_check.actual_dependency_set` and returns any delta as a flag, alongside whatever
    flags the card already recorded. Returns a Result whose `errors` is non-empty iff any flag
    (recorded or freshly computed) is present -- kernel rule 7 (§3.3): non-empty flags is a HARD
    failure, never a disclaimer.
    """
    if not isinstance(card, dict):
        return _result(ok=False, errors=["silent_lift_check: instance is not an object"])

    slc = card.get("silent_lift_check") or {}
    represented = set(slc.get("represented_dependency_set") or [])
    actual = set(slc.get("actual_dependency_set") or [])
    computed_flags = sorted(actual - represented)
    existing_flags = list(slc.get("flags") or [])

    errors = []
    if computed_flags:
        errors.append(
            "silent_lift_check: actual_dependency_set contains node(s) not in represented_dependency_set: "
            f"{computed_flags} -- this IS the silent lift (Q3 misattribution)."
        )
    if existing_flags:
        errors.append(f"silent_lift_check: flags already recorded and non-empty: {existing_flags} (kernel rule 7 -- hard fail, blocks status advancement).")

    res = _result(ok=not errors, errors=errors)
    res["computed_flags"] = computed_flags
    res["existing_flags"] = existing_flags
    return res


# --------------------------------------------------------------------------------------------
# lit_gate
# --------------------------------------------------------------------------------------------

def lit_gate(manifest):
    """S14 literature-review-system accuracy + diversity gates, re-derived from a
    litreview_manifest payload. Returns a Result whose `verdict` is one of the gate_verdict
    values (PASS | PASS_WITH_LIMITS | FAIL | HUMAN_REVIEW).

    Re-checks (not re-trusts) the manifest's own declared `gate.overall` against its inputs:
    - `secondary_citation_ban_audit.violations_found > 0` is a hard block (never PASS) per the
      manifest schema's own allOf.
    - `gate.overall == FAIL` requires a non-empty `blocked_reason`.
    - the declared `gate.overall` must be at least as strict as the worse of `accuracy_gate` and
      `diversity_gate` (never silently upgraded).
    """
    if not isinstance(manifest, dict):
        return _result(ok=False, errors=["lit_gate: instance is not an object"])

    errors = []
    warnings = []
    schema_errors, used_fallback = _schema_validate(manifest, "litreview_manifest.schema.json")
    errors.extend(schema_errors)
    if used_fallback:
        warnings.append("jsonschema not available -- litreview_manifest.schema.json's own allOf gates (blocked_reason/violations) were not run by the schema layer; kernel checks below still ran.")

    gate = manifest.get("gate") or {}
    accuracy_gate = gate.get("accuracy_gate")
    diversity_gate = gate.get("diversity_gate")
    overall = gate.get("overall")

    verdict_rank = {"PASS": 0, "PASS_WITH_LIMITS": 1, "HUMAN_REVIEW": 2, "FAIL": 3}
    worst = max((v for v in (accuracy_gate, diversity_gate) if v in verdict_rank), key=lambda v: verdict_rank[v], default=None)

    violations = (manifest.get("secondary_citation_ban_audit") or {}).get("violations_found", 0)
    if violations and overall == "PASS":
        errors.append(f"lit_gate: secondary_citation_ban_audit.violations_found={violations} but gate.overall is PASS -- hard block violated.")

    if overall == "FAIL" and not gate.get("blocked_reason"):
        errors.append("lit_gate: gate.overall is FAIL but blocked_reason is empty/null.")

    if worst is not None and overall is not None and verdict_rank.get(overall, 0) < verdict_rank[worst]:
        errors.append(
            f"lit_gate: gate.overall ({overall}) is looser than the worse of accuracy_gate/diversity_gate ({worst}) -- never silently upgraded."
        )

    return _result(ok=not errors, verdict=(overall if not errors else "FAIL"), errors=errors, warnings=warnings)


# --------------------------------------------------------------------------------------------
# xenon_ledger_check (MUST-12: Xenon Ledger threshold gate)
# --------------------------------------------------------------------------------------------

_DEFAULT_XENON_LEDGER_THRESHOLD = 3


def xenon_ledger_check(citation_cards, threshold=_DEFAULT_XENON_LEDGER_THRESHOLD):
    """Minimal Xenon Ledger reader (§7.8, MUST-12): counts SCRAMMED citation_cards that are still
    unresolved (no `superseded_by` set) among the citation_cards actually supplied, and hard-fails
    once that count exceeds `threshold`.

    Honest scope disclosure (reviews/ARCH_structure.md, MUST-12): FOUNDATION_v0.5.md's Xenon
    Ledger design (design/REPO_SPEC_v0.5.md) describes a persistent, append-only
    `ledgers/XENON_LEDGER.md` file plus a `schema/xenon_ledger.schema.json` shape and a
    `glosa ledger` CLI verb -- none of those exist on disk yet (confirmed live:
    `ledgers/` is untracked and empty). This function does NOT read such a file -- building the
    on-disk ledger/schema/CLI verb is a separate task, outside this fix's file scope. It instead
    reads the in-memory list of citation_card payloads a caller actually supplies, which is the
    only real, present data source. `validate_citation_card`'s existing per-card
    `xenon_ledger_ref` non-null presence requirement is left unchanged (a SCRAMMED card must still
    name a ref); this function adds the second half MUST-12 named -- a genuine, mechanically
    enforced count/threshold gate over a real citation_card batch -- rather than removing the
    first half or leaving the count promise entirely unimplemented ("pick the simpler honest
    option": this is the option that stays fully inside stdlib + this fix's assigned files while
    still being a real, tested, threshold-enforced check, not a demoted no-op).

    Returns a Result with two extra keys: `unresolved_scrammed_count` and `threshold`.
    """
    cards = [c for c in (citation_cards or []) if isinstance(c, dict)]
    unresolved_scrammed = [c for c in cards if c.get("status") == "SCRAMMED" and not c.get("superseded_by")]
    errors = []
    if len(unresolved_scrammed) > threshold:
        ids = [c.get("id") for c in unresolved_scrammed]
        errors.append(
            f"xenon_ledger_check: {len(unresolved_scrammed)} unresolved SCRAMMED citation_card(s) "
            f"{ids} exceed the threshold of {threshold} -- gate_release blocked until these are "
            "resolved (superseded_by set) or the threshold is explicitly raised by a human call."
        )
    res = _result(ok=not errors, errors=errors)
    res["unresolved_scrammed_count"] = len(unresolved_scrammed)
    res["threshold"] = threshold
    return res


# --------------------------------------------------------------------------------------------
# gate_release
# --------------------------------------------------------------------------------------------

def gate_release(manifest, cards, reviews, citation_cards=None):
    """FOUNDATION §9's `gate_release`. `cards` and `reviews` are lists of claim_card / review_report
    payloads; `manifest` is a release_manifest payload naming which claim_ids it releases.
    `citation_cards` is OPTIONAL (default None): a list of citation_card payloads, used to run
    the MUST-12 Xenon Ledger threshold check (`xenon_ledger_check`) and the MUST-6 D-LENS-UNCITED
    check inside each `validate_claim_card` call; omitting it does not fabricate a pass for either
    -- both gaps are named explicitly in `reasons` instead (see below).
    Returns {"verdict": PASS|PASS_WITH_LIMITS|FAIL|HUMAN_REVIEW, "reasons": [str, ...], "ok": bool,
    "tier": "finite_diagnostic"}.
    """
    reasons = []
    hard_fail = False
    human_review = False

    manifest_res = validate_release_manifest(manifest)
    if not manifest_res["ok"]:
        hard_fail = True
        reasons.extend(f"manifest: {e}" for e in manifest_res["errors"])
    reasons.extend(f"manifest(warning): {w}" for w in manifest_res["warnings"])

    if citation_cards is not None:
        xl_res = xenon_ledger_check(citation_cards)
        if not xl_res["ok"]:
            hard_fail = True
            reasons.extend(f"xenon_ledger: {e}" for e in xl_res["errors"])
    else:
        reasons.append(
            "gate_release: Xenon Ledger threshold check (§7.8, MUST-12) was NOT run -- "
            "citation_cards was not supplied; call xenon_ledger_check(citation_cards) separately "
            "or pass citation_cards=[...] before treating a release as clean."
        )

    cards_by_id = {c.get("claim_id"): c for c in (cards or []) if isinstance(c, dict)}
    claim_ids = ((manifest or {}).get("artifact_refs") or {}).get("claim_ids") or []

    for cid in claim_ids:
        card = cards_by_id.get(cid)
        if card is None:
            hard_fail = True
            reasons.append(f"gate_release: manifest names claim_id {cid!r} but no matching claim_card was supplied")
            continue

        card_res = validate_claim_card(card, citation_cards=citation_cards)
        if not card_res["ok"]:
            hard_fail = True
            reasons.extend(f"claim_card[{cid}]: {e}" for e in card_res["errors"])

        if card.get("shape") == "stub":
            hard_fail = True
            reasons.append(f"claim_card[{cid}]: shape=stub cannot be cited from a release (kernel rule 10)")

        slc_res = silent_lift_check(card)
        if not slc_res["ok"]:
            hard_fail = True
            reasons.extend(f"claim_card[{cid}].silent_lift_check: {e}" for e in slc_res["errors"])

        k_state = card.get("k_state")
        if k_state in ("K1", "K2", "K3"):
            pd_status = (card.get("provenance_dag") or {}).get("status")
            slc_status = (card.get("silent_lift_check") or {}).get("status")
            if pd_status != "run" or slc_status != "run":
                hard_fail = True
                reasons.append(f"claim_card[{cid}]: k_state={k_state} but provenance_dag.status/silent_lift_check.status is not both 'run' (kernel rule 11)")

        # §6.4: an I3+ check on file, or the bounded B4 exception, for this claim's own reviews.
        card_reviews = [r for r in (reviews or []) if isinstance(r, dict) and r.get("claim_ref") == cid]
        best_review_ic = _max_independence_class(card_reviews) if card_reviews else None
        evidence_ic = _max_independence_class((card.get("five_questions") or {}).get("tested", {}).get("evidence_relations") or [])
        strongest = max([x for x in (best_review_ic, evidence_ic) if x], key=_INDEPENDENCE_ORDER.index, default=None)
        exception_ok = _uses_bounded_exception(card)
        if manifest.get("status") in ("Approved-for-Test", "Approved-for-Live") and not exception_ok:
            if strongest is None or _INDEPENDENCE_ORDER.index(strongest) < _INDEPENDENCE_ORDER.index("I3"):
                hard_fail = True
                reasons.append(f"claim_card[{cid}]: no I3+ review/evidence on file and the bounded I2+I4 exception is not in use -- §6.4 mandatory gate not met")

        for rep in card_reviews:
            rep_res = validate_review_report(rep)
            if not rep_res["ok"]:
                hard_fail = True
                reasons.extend(f"review_report[{rep.get('route_id')}] for {cid}: {e}" for e in rep_res["errors"])

        unresolved_dissent = [d for d in (card.get("five_questions") or {}).get("tested", {}).get("dissent_records") or [] if not (d or {}).get("resolved")]
        if unresolved_dissent:
            human_review = True
            reasons.append(f"claim_card[{cid}]: unresolved dissent_records present -- routed to HUMAN_REVIEW")

    reasons.append(
        "gate_release: citation VERIFIED reachability (§6.4) was NOT checked -- gate_release's signature "
        "does not receive citation_card payloads; run cite_check separately before treating a release as clean."
    )

    if hard_fail:
        verdict = "FAIL"
    elif human_review:
        verdict = "HUMAN_REVIEW"
    elif manifest.get("gate_verdict") == "PASS_WITH_LIMITS":
        verdict = "PASS_WITH_LIMITS"
    else:
        verdict = manifest.get("gate_verdict") or "PASS"

    return {"verdict": verdict, "reasons": reasons, "ok": verdict in ("PASS", "PASS_WITH_LIMITS"), "tier": "finite_diagnostic"}


# --------------------------------------------------------------------------------------------
# self_test
# --------------------------------------------------------------------------------------------

def self_test():
    """Run every valid example in schema/examples/ through its matching validate_* function and
    every fixture in schema/examples/fail/ through validate_claim_card, asserting the fail
    fixtures are in fact rejected. Returns a Result; `errors` lists any example that did not
    behave as its filename/`_fail_reason` promises. This is the same self-check
    `tests/test_kernel.py` runs formally -- exposed here as a single callable per FOUNDATION §9's
    named kernel function list.
    """
    errors = []
    warnings = []

    examples_dir = SCHEMA_DIR / "examples"
    fail_dir = examples_dir / "fail"

    pairs = [
        ("claim_card.example.json", validate_claim_card),
        ("review_report.example.json", validate_review_report),
        ("citation_card.example.json", validate_citation_card),
        ("release_manifest.example.json", validate_release_manifest),
        ("blackbox_note.example.json", validate_blackbox_note),
    ]
    for filename, fn in pairs:
        p = examples_dir / filename
        if not p.is_file():
            warnings.append(f"self_test: {filename} not found, skipped")
            continue
        instance = json.loads(p.read_text(encoding="utf-8"))
        res = fn(instance)
        if not res["ok"]:
            errors.append(f"self_test: {filename} expected PASS, got errors: {res['errors']}")

    if fail_dir.is_dir():
        for p in sorted(fail_dir.glob("*.json")):
            instance = json.loads(p.read_text(encoding="utf-8"))
            instance.pop("_fail_reason", None)
            res = validate_claim_card(instance)
            if res["ok"]:
                errors.append(f"self_test: {p.name} was expected to FAIL validate_claim_card but PASSED")

    return _result(ok=not errors, errors=errors, warnings=warnings)


if __name__ == "__main__":  # pragma: no cover
    result = self_test()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["ok"] else 1)
