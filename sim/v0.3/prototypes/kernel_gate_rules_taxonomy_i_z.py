#!/usr/bin/env python3
"""SANDBOX prototype for DAG node kernel.gate-rules-taxonomy-i-z.

Node target (design/DAG_v0.3.yaml, kernel.gate-rules-taxonomy-i-z):
  "Encode the injected-infinity/zero taxonomy (I1-I4 infinity types, Z1-Z4 zero types) and the
  Fail-Able Gate Law (Type-P vs Type-U) as named kernel gate-rule categories, alongside the
  existing contaminated-concept table."
  evidence: kc-base-006, kc-base-008, kc-base-016, kc-base-018, kc-base-034.

kc-base-016 (knowledge/harvest_v0.3/base/kc-base-016.yaml) names the eight non-readouts this
node's rule taxonomy exists to catch when they are smuggled into a claim card as if they were a
readout:
  I1 R-completeness (LUB/Dedekind), I2 h->0, I3 Re,Lambda->infinity, I4 actual +infinity,
  Z1 the point r=0, Z2 reached continuum h=0, Z3 absolute rest v=0/T=0, Z4 the true void.
  ("Reciprocity 1/0=infinity names zero and infinity as one non-readout seen from two sides.")

This prototype is PURE PYTHON, touches nothing under kernel/ schema/ cli/ design/, and is not
wired into the real kernel. It exists only to answer, on this fixed sim/v0.3 corpus: does naming
this I/Z taxonomy as an explicit gate-rule category catch what the current kernel (unmodified)
misses? The kernel today has NO check that reads claim-card prose for injected
infinity/zero absolutes -- rule12/rule15/rule17/rule6(scope) etc. all validate structural fields,
never the free-text statement/hypothesis/evidence-note content -- so this is a genuine coverage
gap, not a duplicate of an existing rule.

Scope (deliberately narrow, matching kc-base-016 exactly): this prototype targets the
`injected_infinity` defect only. The other three defects the harness baseline also misses
(composite_quote, hidden_ai_fill, inflated_bearing) are different defect families
(quote-composition, hidden-AI-authorship, evidence-bearing inflation) with no I1-I4/Z1-Z4
non-readout content -- this node's own `change:` text does not claim to cover them, and this
prototype does not attempt to (see result JSON `defects_targeted`).

Detection method: scan a fixed set of free-text fields on the claim card (statement text +
translation, hypothesis_world text, five_questions.separates.licensing_test.result/notes,
five_questions.tested.falsifier, evidence_relations[].notes, ai_filled.* strings) for regex
patterns naming an I1-I4/Z1-Z4 non-readout presented as an actual/exact value rather than a
readout (bounded, dated, sourced quantity). Patterns are bilingual (EN + TH, since this corpus's
statement text is Thai) and were built by reading kc-base-016's own verbatim taxonomy text, not
reverse-engineered from the corpus's exact wording (though checked against it -- see
DEFECT_KEYWORD_SOURCE note below for the one honesty caveat on that).

Tier of every count in the result JSON: finite_diagnostic -- an exact tally over this fixed,
printed 180-card sim/v0.3 corpus only. Not a claim about recall/false-alarm rate on any other
corpus, and not a claim that this regex approach is the right *implementation* for the kernel
(that would need the real kernel's own text-normalization/i18n handling, which this prototype
does not have or need to have to answer the sandbox question).
"""
from __future__ import annotations

import re
from typing import Any

# --- I1-I4 / Z1-Z4 taxonomy, kc-base-016 verbatim, translated into regex signals -----------------
# Each entry: (code, human label, list of compiled regexes). A hit on ANY regex in a code's list
# is one taxonomy hit for that code. Patterns are deliberately literal/narrow (word-boundary,
# specific phrasing) to keep false alarms low on cards that legitimately discuss limits/statistics
# in a bounded, readout-tagged way (e.g. "n=1 cat, not generalizable" or "K0" tier language, which
# never contains these strings).
_TAXONOMY: list[tuple[str, str, list[re.Pattern]]] = [
    (
        "I4",
        "actual +infinity asserted as a reached value",
        [
            re.compile(r"\binfinit(e|y)\b", re.IGNORECASE),
            re.compile(r"∞"),  # the "∞" glyph itself
            re.compile(r"อนันต์"),  # Thai: infinite/infinity
        ],
    ),
    (
        "I3",
        "Re,Lambda->infinity asymptotic-to-infinity treated as reached",
        [
            re.compile(r"\bapproach(?:es|ing)?\s+infinity\b", re.IGNORECASE),
            re.compile(r"as\s+\w+\s*(?:->|→)\s*(?:infinity|∞)", re.IGNORECASE),
        ],
    ),
    (
        "I2",
        "h->0 infinitesimal-limit treated as reached",
        [
            re.compile(r"(?:->|→)\s*0\b.*\blimit\b", re.IGNORECASE),
            re.compile(r"\binfinitesimal(?:ly)?\b", re.IGNORECASE),
        ],
    ),
    (
        "I1",
        "R-completeness (LUB/Dedekind) asserted as a readout",
        [
            re.compile(r"\bDedekind\s+cut\b", re.IGNORECASE),
            re.compile(r"\bleast\s+upper\s+bound\b", re.IGNORECASE),
            re.compile(r"\bR-complet(e|eness)\b", re.IGNORECASE),
        ],
    ),
    (
        "Z2/Z3",
        "exact/true zero asserted as an actual measured value (exact-zero spacing, absolute rest)",
        [
            re.compile(r"\bexactly\s+zero\b", re.IGNORECASE),
            re.compile(r"\btrue\s+zero\b", re.IGNORECASE),
            re.compile(r"\babsolute\s+zero\b", re.IGNORECASE),
            re.compile(r"\bexact\s+zero\b", re.IGNORECASE),
            re.compile(r"ศูนย์แท้"),  # Thai: "true/exact zero"
        ],
    ),
    (
        "Z1",
        "the point r=0 asserted as a reached zero-dimensional readout",
        [
            re.compile(r"\br\s*=\s*0\b.*\bpoint\b", re.IGNORECASE),
        ],
    ),
    (
        "Z4",
        "the true void / absolute nothing asserted as a reached readout",
        [
            re.compile(r"\btrue\s+void\b", re.IGNORECASE),
            re.compile(r"\babsolute\s+(?:nothing|vacuum)\b", re.IGNORECASE),
        ],
    ),
    (
        "reciprocity-1/0",
        "1/0=infinity reciprocity invoked directly",
        [
            re.compile(r"1\s*/\s*0\s*=\s*(?:∞|infinity)", re.IGNORECASE),
        ],
    ),
]

# Fields scanned for free text. Each path is a tuple of keys/indices-as-strings ("*" means
# "for every item in this list"), read with _walk() below. Kept small and explicit (not a blind
# recursive walk over the whole card) so the prototype's false-alarm surface stays auditable and
# does not accidentally start reading structural/id fields as if they were prose.
_TEXT_FIELD_PATHS: list[tuple] = [
    ("statement", "text"),
    ("statement", "translation", "text"),
    ("hypothesis_world", "text"),
    ("five_questions", "separates", "licensing_test", "result"),
    ("five_questions", "separates", "licensing_test", "notes"),
    ("five_questions", "tested", "falsifier"),
    ("five_questions", "ai_filled", "current_evidence"),
    ("five_questions", "ai_filled", "retrieved_tool_evidence"),
    ("five_questions", "ai_filled", "retained_record_route"),
    ("five_questions", "ai_filled", "model_calibration_assumption"),
    ("five_questions", "ai_filled", "prompt_system_constraint"),
    ("five_questions", "ai_filled", "decision_policy"),
    ("five_questions", "tested", "evidence_relations", "*", "notes"),
    ("non_claims", "*"),
]


def _walk(obj: Any, path: tuple) -> list[tuple[str, str]]:
    """Return [(dotted_path_str, text), ...] for every string reached by following `path`
    through `obj`, expanding "*" over list items. Missing keys / wrong types are skipped
    silently -- this corpus's cards vary in shape (e.g. `shape: stub` cards omit whole
    sections), and a missing field is not itself a taxonomy hit."""
    out: list[tuple[str, str]] = []

    def rec(node: Any, remaining: tuple, path_so_far: str):
        if not remaining:
            if isinstance(node, str):
                out.append((path_so_far, node))
            return
        key, rest = remaining[0], remaining[1:]
        if key == "*":
            if isinstance(node, list):
                for i, item in enumerate(node):
                    rec(item, rest, f"{path_so_far}[{i}]")
            return
        if isinstance(node, dict) and key in node:
            rec(node[key], rest, f"{path_so_far}.{key}" if path_so_far else key)

    rec(obj, path, "")
    return out


def check_gate_rules_taxonomy_i_z(card: dict, citation_cards: list | None = None) -> list[str]:
    """Pure-python sandbox check for the I1-I4/Z1-Z4 injected-infinity/zero taxonomy
    (kc-base-016), matching the DAG node kernel.gate-rules-taxonomy-i-z. Same input shape as
    the real kernel's validate_claim_card (a claim card dict, plus its companion citation
    cards -- the latter are accepted for interface parity but not currently scanned, since
    every injected_infinity fixture in this corpus lives entirely in the claim card's own
    prose, not its citation).

    Returns a list of finding strings, one per (field, taxonomy-code) hit -- never raises,
    never mutates its input.
    """
    findings: list[str] = []
    if not isinstance(card, dict):
        return findings

    hits_seen: set[tuple[str, str]] = set()  # (field_path, code) -> avoid duplicate lines when
    # more than one regex for the same code matches the same field.

    for path in _TEXT_FIELD_PATHS:
        for field_path, text in _walk(card, path):
            for code, label, patterns in _TAXONOMY:
                if (field_path, code) in hits_seen:
                    continue
                for pat in patterns:
                    if pat.search(text):
                        hits_seen.add((field_path, code))
                        findings.append(
                            f"ERROR: gate-rules-taxonomy-i-z: {code} non-readout injected as a "
                            f"reached value ({label}) in {field_path!r}: matched {pat.pattern!r}"
                        )
                        break

    return findings


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("usage: kernel_gate_rules_taxonomy_i_z.py <claim_card.json>", file=sys.stderr)
        raise SystemExit(2)
    card = json.loads(open(sys.argv[1], encoding="utf-8").read())
    for line in check_gate_rules_taxonomy_i_z(card):
        print(line)
