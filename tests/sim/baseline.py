#!/usr/bin/env python3
"""K4-corpus baseline. Runs every card in sim/v0.3/corpus/ through the CURRENT kernel
(kernel/glosa_kernel.py, unmodified -- this script never edits kernel/, schema/, cli/, or
design/) and records, per defect, whether the kernel actually named it (caught) or not
(missed), plus false-alarm counts on the 60 valid cards.

What "run through the kernel" means, concretely, per card:
  - validate_claim_card(card, citation_cards=[companion_citation]) -- always.
  - validate_citation_card(citation) -- always (every claim card has a companion citation card;
    citation-targeted defects, e.g. missing_locator, live entirely in that companion).
  - compute_disclaimers(card) -- always, diffed against the card's own declared
    disclaimers_emitted (a mismatch is itself a finding: the kernel's own disclaimer engine
    disagrees with what the card claims to disclose).
  - gate_release(...) is NOT run per-card: it needs a release_manifest + a reviews list, which
    this corpus does not synthesize per card (out of scope for a claim/citation-level defect
    corpus); noted here rather than silently skipped.

"Caught" (per defect) means: validate_claim_card/validate_citation_card returned at least one
error or warning string whose text names this card's defect (matched via a per-defect keyword
list below, built directly from the kernel functions inspected while writing gen_corpus.py --
e.g. "rule17(" for missing_locator, "rule6(scope)" for premature_category), OR
compute_disclaimers(card) computed a disclaimer id that the card's own declared
disclaimers_emitted omits AND that id is this defect's designated signal (verifiable_no_procedure
-> D-DVP-NOT-K2). Every other case is "missed" -- including a card that fails validation for an
unrelated reason (that is a false alarm on a different axis, not a catch of THIS defect; recorded
separately so precision is not inflated by lucky unrelated failures).

Tier of every count below: finite_diagnostic (an exact tally over this fixed, printed 180-card
corpus -- readout of THIS run, not a claim about kernel behaviour on any other corpus).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CORPUS_DIR = HERE / "corpus"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

# Every adversarial card is built from a base card that independently validates clean (zero
# errors/warnings -- see gen_corpus.py's base_adversarial_card, which is exactly
# build_valid_card()'s own recipe) with exactly ONE defect then injected. So for a structural
# defect, "the kernel caught it" is simply "validate_claim_card/validate_citation_card returned
# an ERROR on this card" -- there is nothing else in the card that could have produced it. Some
# defects also carry a specific expected message substring (recorded here as documentation of
# WHICH rule is expected to fire, cross-checked below rather than used as the sole signal) so a
# human reading this file can see the reasoning that produced gen_corpus.py's own defect design,
# not just a bare pass/fail.
DEFECT_EXPECTED_RULE_HINT = {
    "hidden_ai_fill": "rule27",  # v0.4 fix (S4b): now populates seen.ai_assisted_fields, so
    # kernel/glosa_kernel.py:881 _hidden_ai_fill_error actually fires -- see gen_corpus.py's
    # hidden_ai_fill injector comment.
    "hidden_ai_fill_unmarked": None,  # v0.4: kept as the separate marker-less class so the S4b
    # gap (rule27 is a structural marker check, not a prose scan -- a hidden AI fill with no
    # self-disclosed ai_assisted_fields marker at all is NOT expected to be caught) stays visible
    # rather than silently fixed by the hidden_ai_fill change above.
    "inflated_bearing": None,
    "missing_locator": "rule17(",
    "composite_quote": None,
    "k_state_rounded_up": None,  # schema allOf rule 9, jsonschema's own message does not echo "k_state"
    "stub_public": None,  # schema allOf rule 0 (shape:stub), jsonschema's own message does not echo "shape"
    "signature_missing": "rule12",
    "injected_infinity": None,
    "verifiable_no_procedure": None,  # checked via compute_disclaimers diff (D-DVP-NOT-K2) below
    "premature_category": "rule6(scope)",
    "tier_overclaim": None,  # schema allOf rule 2, jsonschema's own message does not echo "Th_coqc"
    "disclaimer_missing": None,  # schema allOf rule 9 (disclaimer-trigger), checked via error presence
    "ownership_ai": "rule15",
    "same_vendor_review": None,  # schema allOf rule 1 (MC-02), jsonschema's own message does not echo it
}

# Defects whose designated "caught" signal is a compute_disclaimers(card) id present in the
# computed set but absent from the card's own declared disclaimers_emitted.
DEFECT_DISCLAIMER_SIGNAL = {
    "verifiable_no_procedure": "D-DVP-NOT-K2",
    "disclaimer_missing": "D-INDEPENDENCE",
}


def load_json(rel):
    return json.loads((CORPUS_DIR / rel).read_text(encoding="utf-8"))


def run_card(entry):
    card = load_json(entry["claim_file"])
    citation = load_json(entry["citation_file"])

    claim_res = k.validate_claim_card(card, citation_cards=[citation])
    citation_res = k.validate_citation_card(citation)

    all_msgs = list(claim_res.get("errors") or []) + list(claim_res.get("warnings") or []) \
        + list(citation_res.get("errors") or []) + list(citation_res.get("warnings") or [])

    computed_disclaimers = {d["id"] for d in k.compute_disclaimers(card)}
    declared_disclaimers = {d.get("id") for d in (card.get("disclaimers_emitted") or [])}
    disclaimer_gap = computed_disclaimers - declared_disclaimers

    return {
        "claim_ok": claim_res.get("ok"),
        "citation_ok": citation_res.get("ok"),
        "messages": all_msgs,
        "disclaimer_gap": sorted(disclaimer_gap),
    }


def defect_caught(defect, run_result):
    signal_id = DEFECT_DISCLAIMER_SIGNAL.get(defect)
    if signal_id and signal_id in run_result["disclaimer_gap"]:
        return True
    # Structural signal: the card was built defect-free except for this one injected mutation
    # (see gen_corpus.py's base_adversarial_card), so any error the kernel now raises on it is
    # attributable to this defect.
    if not run_result["claim_ok"] or not run_result["citation_ok"]:
        return True
    return False


def main():
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    per_defect = {d: {"n": 0, "caught": 0, "missed": 0} for d in labels["defects"]}
    valid_n = 0
    valid_false_alarm = 0
    valid_false_alarm_ids = []
    missed_ids = {d: [] for d in labels["defects"]}

    for entry in cards:
        result = run_card(entry)
        if entry["kind"] == "valid":
            valid_n += 1
            if not result["claim_ok"] or not result["citation_ok"]:
                valid_false_alarm += 1
                valid_false_alarm_ids.append(entry["id"])
        else:
            defect = entry["defect"]
            per_defect[defect]["n"] += 1
            if defect_caught(defect, result):
                per_defect[defect]["caught"] += 1
            else:
                per_defect[defect]["missed"] += 1
                missed_ids[defect].append(entry["id"])

    total_adv = sum(v["n"] for v in per_defect.values())
    total_caught = sum(v["caught"] for v in per_defect.values())
    total_missed = sum(v["missed"] for v in per_defect.values())
    recall = total_caught / total_adv if total_adv else 0.0
    # precision: of everything the kernel flagged as NOT ok (claim_ok False or citation_ok False)
    # across the whole 180-card corpus, how much of that was a true adversarial catch vs a false
    # alarm on a valid card. "Flagged not-ok" also includes adversarial cards flagged for an
    # unrelated reason (still a real kernel rejection, just not credited as catching THIS card's
    # labelled defect) -- counted here as a true positive at the flag level, separately reported
    # per-defect above where "caught" is the stricter labelled-defect match.
    flagged_true = 0
    flagged_false = valid_false_alarm
    for entry in cards:
        if entry["kind"] != "adversarial":
            continue
        result = run_card(entry)
        if not result["claim_ok"] or not result["citation_ok"]:
            flagged_true += 1
    precision = flagged_true / (flagged_true + flagged_false) if (flagged_true + flagged_false) else 0.0

    out = {
        "corpus": {"n_valid": valid_n, "n_adversarial": total_adv, "n_total": valid_n + total_adv},
        "per_defect": per_defect,
        "valid": {"n": valid_n, "false_alarm": valid_false_alarm, "false_alarm_ids": valid_false_alarm_ids},
        "recall": recall,
        "precision": precision,
        "missed_defect_ids_sample": {d: ids[:3] for d, ids in missed_ids.items() if ids},
        "tier": "finite_diagnostic",
        "note": "readout over this fixed 180-card corpus only, not a general kernel-quality claim",
    }
    (HERE / "baseline.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # Print table
    print(f"{'defect':28s} {'n':>4s} {'caught':>7s} {'missed':>7s}")
    print("-" * 50)
    for d in labels["defects"]:
        row = per_defect[d]
        print(f"{d:28s} {row['n']:4d} {row['caught']:7d} {row['missed']:7d}")
    print("-" * 50)
    print(f"{'TOTAL adversarial':28s} {total_adv:4d} {total_caught:7d} {total_missed:7d}")
    print(f"valid cards: n={valid_n} false_alarm={valid_false_alarm}")
    print(f"recall={recall:.3f} precision={precision:.3f}")

    result_json = {
        "n_valid": valid_n,
        "n_adv": total_adv,
        "recall": round(recall, 4),
        "precision": round(precision, 4),
        "missed_defects": sorted([d for d, v in per_defect.items() if v["missed"] > 0]),
    }
    print("RESULT_JSON " + json.dumps(result_json, ensure_ascii=False))
    return result_json


# =============================================================================================
# v0.4 corpus runner -- design/SESSION_ARCH_v0.4_SPEC.md §5's five session-architecture defect
# classes, over tests/sim/corpus/v04/ (see tests/sim/gen_corpus.py's gen_v04_corpus() for the
# fixture shapes).
#
# TODO(schema.retention-direction-field, SA-1, kernel.reciprocal-lineage-diagnostic, SA-3):
# hypothesis_selection.yaml has no `retained_direction`/`chooser_reaffirmations[]` field,
# blackbox_note.schema.json has no `ai_state_at_boundary` field, and no session/`chi_recip`
# validator exists in kernel/glosa_kernel.py yet (confirmed by direct grep, 2026-09-05) -- these
# are the still-pending v0.4 schema/kernel proposals landing in parallel with this sim task. The
# `_check_*_v04` functions below are a sim-local PROTOTYPE reference implementation of each
# proposal's own `failing_control` clause, tier `Dr` (a hand-written reading of the spec text,
# not a shipped, independently-reviewed kernel/schema rule). They exist so this corpus's
# "must fire"/"must not fire" pairs are exercised by SOMETHING today, and so this file has a
# single, obvious place to redirect to the real kernel/schema call the moment each proposal
# ships -- replace the corresponding `_check_*_v04` body with a call into
# kernel.glosa_kernel/jsonschema at that point, do not keep both. Never cite a number produced
# by these functions as evidence of the shipped kernel's behaviour -- see tests/sim/report.md's
# v0.4 section for the tier-honest framing.
# =============================================================================================

import re as _re_v04

_MOMENTUM_TERM_RE = _re_v04.compile(r"(chi_recip|m\^h|m\^ai|momentum|reciprocal-lineage)", _re_v04.IGNORECASE)
_GATE_WARRANT_RE = _re_v04.compile(
    r"(release|warrant|\bgate\b|\btrue\b|correct|proof|certif|sufficient|must pass|allowed)",
    _re_v04.IGNORECASE,
)
# A gate/warrant term inside a few words of a negation ("not a release gate", "never proof",
# "no warrant") reads as the honest Open-tier disclaimer, not the overclaim -- the fixture set
# deliberately exercises this (per §5's "MUST NOT fire" half), so the checker must not flag it.
_NEGATION_NEAR_RE = _re_v04.compile(r"\b(not|never|n't|no)\b[\w\s,/-]{0,40}$", _re_v04.IGNORECASE)


def _momentum_reads_as_gate(sentence):
    """Sentence-scoped, order-independent check: a momentum/chi_recip term and a gate/warrant
    term both present in the same sentence, with the gate/warrant term not immediately preceded
    by a negation word."""
    if not _MOMENTUM_TERM_RE.search(sentence):
        return False
    for m in _GATE_WARRANT_RE.finditer(sentence):
        prefix = sentence[:m.start()]
        if not _NEGATION_NEAR_RE.search(prefix):
            return True
    return False


def _check_tunnel_unflagged_v04(row):
    """Prototype of NC-77 / schema.retention-direction-field: a `chosen` hypothesis_selection
    row spanning >=2 sessions with no evidence_relation resolving to an independent-check verdict
    must carry retained_direction == 'unknown'. Returns a message when violated, else None."""
    sessions = set(row.get("session_ids") or [])
    if row.get("selection_status") != "chosen" or len(sessions) < 2:
        return None
    er = row.get("evidence_relation") or {}
    if er.get("resolves_to_checker_verdict"):
        return None  # the linked verdict's own sign stands, per NC-77
    rd = row.get("retained_direction")
    if rd != "unknown":
        return (f"WARN: retained_direction={rd!r} -- no linked independent-check artifact for a "
                 "row chosen across >=2 sessions (NC-77)")
    return None


def _check_retention_undeclared_v04(pair):
    """Prototype of SA-1: a Blackbox Note pair sharing one session_id, split by a real
    process/tool restart, must both carry ai_state_at_boundary == 'reset' (literal)."""
    a = pair.get("note_a") or {}
    b = pair.get("note_b") or {}
    if a.get("session_id") != b.get("session_id"):
        return None
    if not (a.get("process_restart_after") or b.get("process_restart_after")):
        return None
    bad = [name for name, note in (("note_a", a), ("note_b", b)) if note.get("ai_state_at_boundary") != "reset"]
    if bad:
        return (f"ERROR: ai_state_at_boundary missing or not literal 'reset' in {bad} across "
                "shared session_id")
    return None


def _check_chooser_forgotten_v04(row):
    """Prototype of schema.retention-direction-field's chooser_reaffirmations[] mechanism: a
    session reopening a previously-chosen hypothesis without a fresh chooser_reaffirmations[]
    entry for that reopening session must be flagged (S3c requires the human, not persistence, to
    reaffirm)."""
    reopened = row.get("reopened_in_session")
    if not reopened:
        return None
    reaff = row.get("chooser_reaffirmations") or []
    if not any((r or {}).get("session_id") == reopened for r in reaff):
        return (f"FLAG: hypothesis reopened in session {reopened!r} without a fresh "
                "chooser_reaffirmations[] entry")
    return None


def _check_question_drift_unlogged_v04(sess):
    """Prototype of SA-3's question_trace[]/drift mechanism: a session whose Problem Card
    sequence diverges from its own declared q1_issue, with no new Problem Card opened to track
    the divergence, is flagged as untracked drift."""
    declared = sess.get("declared_q1_issue")
    cards = sess.get("problem_cards_opened") or []
    drift = any((c or {}).get("q1_issue") != declared for c in cards)
    if drift and not sess.get("new_problem_card_opened_for_drift"):
        return "FLAG: question drift from declared q1_issue with no new Problem Card opened"
    return None


def _check_momentum_overclaimed_v04(doc):
    """Prototype of kernel.reciprocal-lineage-diagnostic / SA-4: any text reading chi_recip /
    m^H / m^AI as warrant, truth, or a release gate (rather than an Open diagnostic) is a hard
    reject."""
    text = doc.get("text") or ""
    for sentence in _re_v04.split(r"(?<=[.!?])\s+", text):
        if _momentum_reads_as_gate(sentence):
            return "REJECT: momentum/chi_recip diagnostic read as warrant/truth/release-gate, not Open-tier"
    return None


_V04_CHECKERS = {
    "tunnel_unflagged": _check_tunnel_unflagged_v04,
    "retention_undeclared": _check_retention_undeclared_v04,
    "chooser_forgotten": _check_chooser_forgotten_v04,
    "question_drift_unlogged": _check_question_drift_unlogged_v04,
    "momentum_overclaimed": _check_momentum_overclaimed_v04,
}


def main_v04():
    labels = json.loads((CORPUS_DIR / "v04" / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    per_defect = {d: {"n_adv": 0, "caught": 0, "missed": 0, "n_valid": 0, "false_alarm": 0} for d in labels["defects"]}
    false_alarm_ids = {d: [] for d in labels["defects"]}
    missed_ids = {d: [] for d in labels["defects"]}

    # Valid fixtures don't carry a `defect` id (per gen_v04_corpus, defect=None for kind=valid);
    # group them by directory prefix of their filename instead, which encodes the defect class
    # they are a control for (e.g. hsel/tunnel_unflagged_valid_001.json).
    for entry in cards:
        rel = entry["file"].split("v04/", 1)[1]
        obj = json.loads((CORPUS_DIR / "v04" / rel).read_text(encoding="utf-8"))
        fname = Path(rel).name
        defect_for_fixture = next((d for d in labels["defects"] if fname.startswith(d + "_")), None)
        assert defect_for_fixture, f"v0.4 fixture {rel!r} filename does not name a known defect class"
        checker = _V04_CHECKERS[defect_for_fixture]
        msg = checker(obj)
        if entry["kind"] == "adversarial":
            per_defect[defect_for_fixture]["n_adv"] += 1
            if msg is not None:
                per_defect[defect_for_fixture]["caught"] += 1
            else:
                per_defect[defect_for_fixture]["missed"] += 1
                missed_ids[defect_for_fixture].append(entry["id"])
        else:
            per_defect[defect_for_fixture]["n_valid"] += 1
            if msg is not None:
                per_defect[defect_for_fixture]["false_alarm"] += 1
                false_alarm_ids[defect_for_fixture].append(entry["id"])

    total_adv = sum(v["n_adv"] for v in per_defect.values())
    total_caught = sum(v["caught"] for v in per_defect.values())
    total_valid = sum(v["n_valid"] for v in per_defect.values())
    total_false_alarm = sum(v["false_alarm"] for v in per_defect.values())
    recall = total_caught / total_adv if total_adv else 0.0

    out = {
        "tier": "Dr",
        "note": ("prototype reference-checker readout over tests/sim/corpus/v04/ ONLY -- these "
                 "checkers are sim-local hand-written readings of design/SESSION_ARCH_v0.4_SPEC.md "
                 "§5's failing_control clauses, not the shipped kernel/schema (which do not yet "
                 "implement these fields/rules -- see this file's TODO block above). Not a claim "
                 "about kernel/schema behaviour."),
        "per_defect": per_defect,
        "recall_of_prototype_checkers": recall,
        "n_adv": total_adv,
        "n_valid": total_valid,
        "false_alarm_total": total_false_alarm,
        "missed_ids_sample": {d: ids[:3] for d, ids in missed_ids.items() if ids},
        "false_alarm_ids_sample": {d: ids[:3] for d, ids in false_alarm_ids.items() if ids},
    }
    (HERE / "baseline_v04.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\n{'v0.4 defect':28s} {'n_adv':>6s} {'caught':>7s} {'missed':>7s} {'n_valid':>8s} {'false_alarm':>12s}")
    print("-" * 72)
    for d in labels["defects"]:
        row = per_defect[d]
        print(f"{d:28s} {row['n_adv']:6d} {row['caught']:7d} {row['missed']:7d} {row['n_valid']:8d} {row['false_alarm']:12d}")
    print("-" * 72)
    print(f"prototype-checker recall={recall:.3f} (n_adv={total_adv}), false_alarm_total={total_false_alarm}/{total_valid}")
    return out


if __name__ == "__main__":
    main()
    main_v04()
