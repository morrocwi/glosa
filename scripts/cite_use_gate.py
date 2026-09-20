#!/usr/bin/env python3
"""glosa -- citation-use gate: ADMIT / HOLD / REJECT verdict over cite_check_adhoc.py's output.

tier: Dr (specified; independently unreviewed, no §5.4 human spot-check applied to its
own verdicts -- see DISCLOSURE below). No new equation or theorem is registered by this
module -- pure classification/dispatch over an existing checker's output, so
EPIS-TOLEDO-FIRST / EPIS-REUSE-PIPELINE do not apply.

Global by design, not Thai-specific: this gate only reads existence_tier / venue_tier /
claim_match / backend_errors, fields cite_check_adhoc.py already produces the same way
for every source worldwide (Crossref, OpenAlex, PubMed, Semantic Scholar, arXiv, Zenodo,
EuropePMC, url-fetch, and the optional TCI/ThaiJO venue-tier readings). No branch in this
file special-cases a country or language -- a Thai-language source and any other source
flow through the identical rule set. This closes the gap the founder named on 2026-09-20
while reviewing a pasted proposal to absorb `thai-cite-engine`: GLOSA already had every
axis below as *ontology* (evidence_relation.schema.json's `bearing`, claim_card's
`claim_match`, venue_tier's honest-ceiling tiers) but not wired together as one runtime
verdict + coverage readout. thai-cite-engine's own concept-validation run (2026-09-20,
see ~/ANSE.ASIA/thai-cite-engine/docs/HANDOFF_2026-09-20.md) came back NO-GO on exactly
this kind of gate (its G6 compared loose context instead of candidate identity) -- this
module is a fresh implementation reusing GLOSA's own already-scored existence_tier and
claim_match fields, not a port of that broken code.

WHAT THIS IS NOT: an independent check, a release approval, or a substitute for a real
citation_card.yaml + §5.4 human spot-check. See maker-checker-gate / glosa-independent-check
-- ADMIT here means "mechanically consistent enough to proceed," never "checked."

Verdict rules (existence_tier and claim_match come straight from cite_check_adhoc.py,
never re-derived here):

  REJECT  existence_tier == NOT_FOUND
          -- no real source record was found by any backend; nothing to cite.

  HOLD    existence_tier in (AMBIGUOUS, CHECK_ERROR)
          -- either two+ distinct candidates are too close to call, or a backend errored
          and no other backend completed a clean check. Uncertain, not disproven.
  HOLD    existence_tier in (VERIFIED_EXACT, VERIFIED_FUZZY) and a claim was given but
          claim_match.claim_match_verified is False
          -- source exists and is real, but does not verifiably support the stated claim.
          SourceExistence != ClaimSupport (glosa non-collapse rule) -- this is exactly the
          case that must never silently read as ADMIT or REJECT.
  HOLD    existence_tier in (VERIFIED_EXACT, VERIFIED_FUZZY) and no claim was given
          -- gate_scope is EXISTENCE_ONLY; ADMIT would overstate what was checked, so a
          bare existence match without a claim to check against HOLDs, not ADMITs, unless
          the caller explicitly opts into existence-only admission (--existence-only-ok).

  ADMIT   existence_tier in (VERIFIED_EXACT, VERIFIED_FUZZY) and
          (claim given and claim_match.claim_match_verified is True), OR
          (no claim given and --existence-only-ok was passed)

coverage_readout (global; distinct from existence_tier -- this describes SEARCH COMPLETENESS,
not what was found, per the glosa rule LOCAL_EVIDENCE_NOT_FOUND != NO_LOCAL_EVIDENCE_EXISTS):

  SEARCHED_OK     every backend that was applicable to this identifier completed without
                  error (existence_tier itself may still be NOT_FOUND -- that is a real,
                  clean "not found," not a gap in the search).
  UNAVAILABLE     existence_tier == CHECK_ERROR, or backend_errors is non-empty AND the
                  winning candidate (if any) came from a backend other than the one(s)
                  that errored -- i.e. some backend that should have had a say did not
                  get to. A "not found" verdict is untrustworthy until this clears.
  NOT_ATTEMPTED   the claim axis only: no --claim was given, so claim_match coverage is
                  NOT_ATTEMPTED, independent of the existence axis's own coverage.

usage:
  cite_use_gate.py --reference "<text>" [--doi <doi>] [--pmid <pmid>] [--claim "<sentence>"]
                    [--vendor claude|codex|gemini] [--tci-csv <path>] [--quartile-csv <path>]
                    [--existence-only-ok]
"""
import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cite_check_adhoc import check_reference  # reused by import, not duplicated

DISCLOSURE = (
    "MECHANICAL_GATE_ONLY -- ADMIT/HOLD/REJECT is a classification over "
    "cite_check_adhoc.py's fields, not an independent check (glosa-independent-check) "
    "and not release approval; a real citation_card.yaml + maker-checker-gate review "
    "is still required before status: VERIFIED or a public claim."
)


def gate(check_result, existence_only_ok=False):
    """Pure function over check_reference()'s output dict -- takes no network action of its
    own, so it is safe to call repeatedly and on cached/replayed results."""
    existence_tier = check_result["existence_tier"]
    backend_errors = check_result.get("backend_errors") or []
    claim_match = check_result.get("claim_match")
    has_claim = "claim" in check_result

    # -- coverage_readout: search completeness, independent of what was found --
    if existence_tier == "CHECK_ERROR":
        existence_coverage = "UNAVAILABLE"
    elif backend_errors and not check_result.get("best_match"):
        # a backend errored and no other backend produced a usable candidate either --
        # the same condition _classify() itself treats as CHECK_ERROR upstream, kept here
        # as a defensive second read rather than trusting one string field alone.
        existence_coverage = "UNAVAILABLE"
    else:
        existence_coverage = "SEARCHED_OK"

    claim_coverage = "NOT_ATTEMPTED" if not has_claim else "SEARCHED_OK"

    # -- verdict --
    reasons = []
    if existence_tier == "NOT_FOUND":
        verdict = "REJECT"
        gate_scope = "EXISTENCE_ONLY" if not has_claim else "EXISTENCE_AND_CLAIM_MATCH"
        reasons.append("existence_tier=NOT_FOUND: no backend produced a matching source record")
    elif existence_tier in ("AMBIGUOUS", "CHECK_ERROR"):
        verdict = "HOLD"
        gate_scope = "EXISTENCE_ONLY" if not has_claim else "EXISTENCE_AND_CLAIM_MATCH"
        reasons.append(f"existence_tier={existence_tier}: identity not settled mechanically")
    elif existence_tier in ("VERIFIED_EXACT", "VERIFIED_FUZZY"):
        if has_claim:
            gate_scope = "EXISTENCE_AND_CLAIM_MATCH"
            if claim_match and claim_match.get("claim_match_verified"):
                verdict = "ADMIT"
                reasons.append("existence verified and claim_match_verified=True")
            else:
                verdict = "HOLD"
                reasons.append(
                    "existence verified but claim_match_verified is False or missing -- "
                    "SourceExistence != ClaimSupport, source is real but does not verifiably "
                    "back the stated claim"
                )
        else:
            gate_scope = "EXISTENCE_ONLY"
            if existence_only_ok:
                verdict = "ADMIT"
                reasons.append(
                    "existence verified, no claim was given, caller opted into "
                    "existence-only admission (--existence-only-ok)"
                )
            else:
                verdict = "HOLD"
                reasons.append(
                    "existence verified but no claim was checked against it -- ADMIT "
                    "without a claim would overstate what this gate actually checked; "
                    "pass --existence-only-ok if a bare existence match is all this use needs"
                )
    else:
        # Any existence_tier value not enumerated above (future addition to
        # cite_check_adhoc.py) fails closed to HOLD, never to a silent ADMIT.
        verdict = "HOLD"
        gate_scope = "EXISTENCE_ONLY" if not has_claim else "EXISTENCE_AND_CLAIM_MATCH"
        reasons.append(f"existence_tier={existence_tier!r} not recognized by this gate -- fail-closed to HOLD")

    return {
        "verdict": verdict,
        "gate_scope": gate_scope,
        "reasons": reasons,
        "coverage_readout": {
            "existence": existence_coverage,
            "claim_match": claim_coverage,
        },
        "disclosure": DISCLOSURE,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--reference", required=True)
    ap.add_argument("--doi", default=None)
    ap.add_argument("--pmid", default=None)
    ap.add_argument("--claim", default=None)
    ap.add_argument("--vendor", default="claude", choices=["claude", "codex", "gemini"])
    ap.add_argument("--tci-csv", default=None)
    ap.add_argument("--quartile-csv", default=None)
    ap.add_argument("--existence-only-ok", action="store_true",
                     help="allow ADMIT on a verified existence match with no --claim given")
    a = ap.parse_args()

    check_result = check_reference(
        a.reference, doi=a.doi, pmid=a.pmid, claim=a.claim, vendor=a.vendor,
        tci_csv=a.tci_csv, quartile_csv=a.quartile_csv,
    )
    gate_result = gate(check_result, existence_only_ok=a.existence_only_ok)

    out = dict(check_result)
    out["gate"] = gate_result
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
