"""Test for methodology/H3_falsifier_sim.py (H3 falsifier simulation, proxy, N=40).

Per this task's own instruction, this test asserts only that the script RUNS and reports BOTH
numbers -- it must never assert that H3 "wins" (route B out-catching route A is not something
this test enforces; the script's own falsifier direction is reported honestly whichever way it
comes out, and a future kernel change could legitimately flip it).

Fail-Able Gate Law (BBL-119) controls: a passing control (clean fixture) must score zero catches
on both routes, and a failing control (a known hidden_ai_fill fixture) must score at least one
catch on route B (rule27) -- these are the failing-control + passing-control pair for this sim.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "methodology"))

import H3_falsifier_sim as h3  # noqa: E402


def test_selection_is_exactly_40_cards():
    selection = h3.load_selection()
    assert len(selection) == 40
    from collections import Counter

    counts = Counter(e["label"]["defect"] for e in selection)
    for defect in h3.DEFECT_CLASSES:
        assert counts[defect] == 8, f"expected 8 '{defect}' cards, found {counts[defect]}"


def test_run_reports_both_route_numbers():
    result = h3.run()
    assert result["n"] == 40
    assert result["n_expected"] == 40
    assert isinstance(result["route_a_caught_total"], int)
    assert isinstance(result["route_b_caught_total"], int)
    # Both numbers must actually be present and reported -- this is the only outcome asserted.
    assert "route_a_caught_total" in result and "route_b_caught_total" in result
    assert result["h3_falsifier_direction"] in (
        "SUPPORTED_IN_THIS_PROXY (route B out-caught route A)",
        "DEFEATED_IN_THIS_PROXY (route B did not out-catch route A)",
    )
    assert result["tier"] == "finite_diagnostic"
    assert "PROXY" in result["proxy_disclosure"]
    assert "real cross-vendor" in result["proxy_disclosure"] or "real I3" in result["proxy_disclosure"]


def test_run_never_asserts_h3_wins_itself():
    """This test must not fail if route B under-catches route A -- H3 not winning is a legitimate,
    reportable outcome, not a test failure. We only check the field exists and is one of the two
    honest directions (covered above); this test documents the intent explicitly so a future
    editor does not accidentally add a `assert total_b > total_a` here."""
    result = h3.run()
    # No assertion here compares route_a_caught_total to route_b_caught_total's ORDER.
    assert result["difference_b_minus_a"] == result["route_b_caught_total"] - result["route_a_caught_total"]


def test_passing_control_scores_zero_on_both_routes():
    claim, citation = h3.build_passing_control()
    a = h3.route_a_maker_completeness_catches(claim, citation)
    b = h3.route_b_kernel_rules_catches(claim, citation)
    assert a == []
    assert b == []


def test_failing_control_is_caught_by_route_b_rule27():
    claim, citation = h3.build_failing_control()
    b = h3.route_b_kernel_rules_catches(claim, citation)
    assert any(f.startswith("rule27") for f in b)


def test_main_writes_results_json_and_report_section(tmp_path, monkeypatch):
    result = h3.run()
    h3.write_outputs(result)
    assert h3.RESULTS_PATH.exists()
    on_disk = json.loads(h3.RESULTS_PATH.read_text(encoding="utf-8"))
    assert on_disk["n"] == 40
    assert on_disk["route_a_caught_total"] == result["route_a_caught_total"]
    assert on_disk["route_b_caught_total"] == result["route_b_caught_total"]

    report_text = h3.REPORT_PATH.read_text(encoding="utf-8")
    assert "## H3 falsifier simulation (proxy)" in report_text
    assert report_text.count("## H3 falsifier simulation (proxy)") == 1
    assert "route A caught" in report_text
    assert "route B caught" in report_text
    assert "PROXY" in report_text
