"""tests/test_reproduction_card.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers the Reproduction Ledger (P22): `schema/reproduction_card.schema.json`,
`kernel.glosa_kernel.validate_reproduction_card` + `kernel.glosa_kernel.aowc_gate_check`,
`scripts/repro_check.py`'s hash/tolerance/execute/verify/to_ret_rows functions, and `cli/glosa`'s
`repro new/run/verify/to-ret` verbs end-to-end (subprocess, in an isolated tmp directory -- never
against this repo's own `cases/repro/`).
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_DIR = REPO_ROOT / "kernel"
SCRIPTS_DIR = REPO_ROOT / "scripts"
CLI_PATH = REPO_ROOT / "cli" / "glosa"
EXAMPLES_DIR = REPO_ROOT / "schema" / "examples"

for d in (KERNEL_DIR, SCRIPTS_DIR):
    if str(d) not in sys.path:
        sys.path.insert(0, str(d))

import glosa_kernel as k  # noqa: E402
import repro_check as rc  # noqa: E402


def load_example(name):
    return json.loads((EXAMPLES_DIR / name).read_text(encoding="utf-8"))


def run_cli(args, cwd):
    proc = subprocess.run(
        [sys.executable, str(CLI_PATH)] + args, cwd=str(cwd), capture_output=True, text=True,
    )
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        payload = {"_raw_stdout": proc.stdout, "_raw_stderr": proc.stderr}
    return proc.returncode, payload


# --------------------------------------------------------------------------------------------
# Schema + kernel validation
# --------------------------------------------------------------------------------------------

class TestSchemaAndKernelValidation(unittest.TestCase):
    def test_example_card_passes(self):
        card = load_example("reproduction_card.example.json")
        res = k.validate_reproduction_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertEqual(res["tier"], "finite_diagnostic")

    def test_fail_fixture_ai_at_runtime_nonzero_is_rejected(self):
        card = json.loads(
            (EXAMPLES_DIR / "fail" / "fail_reproduction_card_ai_at_runtime_nonzero.json").read_text(encoding="utf-8")
        )
        card.pop("_fail_reason", None)
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"])

    def test_toledo_codes_empty_requires_pending_status(self):
        card = load_example("reproduction_card.example.json")
        card["toledo_codes"] = []
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"], "empty toledo_codes[] with no status:pending_toledo_code must fail")
        card["status"] = "pending_toledo_code"
        res2 = k.validate_reproduction_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_pending_status_requires_null_run(self):
        card = load_example("reproduction_card.example.json")
        card["result"]["status"] = "PENDING"
        # run is still filled from the example -- this must fail (run filled + PENDING result).
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("still PENDING" in e for e in res["errors"]), res["errors"])

    def test_run_null_requires_pending_status(self):
        card = load_example("reproduction_card.example.json")
        card["run"] = None
        # result.status is still "PASS" from the example -- must fail (run null but status != PENDING).
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("run is still null" in e for e in res["errors"]), res["errors"])

    def test_declared_at_after_run_date_fails(self):
        card = load_example("reproduction_card.example.json")
        card["preregistered_prediction"]["declared_at"] = "2027-01-01T00:00:00+00:00"
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("AFTER run.date" in e for e in res["errors"]), res["errors"])

    def test_unparseable_dates_warn_not_error(self):
        card = load_example("reproduction_card.example.json")
        card["preregistered_prediction"]["declared_at"] = "not-a-date"
        res = k.validate_reproduction_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertTrue(any("NOT checked" in w for w in res["warnings"]), res["warnings"])

    def test_external_oracle_requires_pin_once_result_filled(self):
        card = load_example("reproduction_card.example.json")
        card["oracle"]["doi_or_url"] = None
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("requires the oracle pin" in e for e in res["errors"]), res["errors"])

    def test_environment_packages_rejects_unlisted_names(self):
        card = load_example("reproduction_card.example.json")
        card["environment"]["packages"] = {"requests": "2.0"}
        res = k.validate_reproduction_card(card)
        self.assertFalse(res["ok"])

    def test_environment_packages_accepts_mpmath_and_numpy(self):
        card = load_example("reproduction_card.example.json")
        card["environment"]["packages"] = {"mpmath": "1.3.0", "numpy": "2.0.0"}
        res = k.validate_reproduction_card(card)
        self.assertTrue(res["ok"], res["errors"])


# --------------------------------------------------------------------------------------------
# aowc_gate_check (R6)
# --------------------------------------------------------------------------------------------

class TestAowcGateCheck(unittest.TestCase):
    def test_passing_card_holds_aowc(self):
        card = load_example("reproduction_card.example.json")
        held, reason = k.aowc_gate_check(card)
        self.assertTrue(held, reason)
        self.assertTrue(reason.startswith("HEURISTIC:"))

    def test_coq_kernel_oracle_never_holds_aowc(self):
        card = load_example("reproduction_card.example.json")
        card["oracle"]["kind"] = "coq_kernel"
        held, reason = k.aowc_gate_check(card)
        self.assertFalse(held)
        self.assertIn("not an external-oracle kind", reason)

    def test_error_result_never_holds_aowc(self):
        card = load_example("reproduction_card.example.json")
        card["result"]["status"] = "ERROR"
        held, reason = k.aowc_gate_check(card)
        self.assertFalse(held)
        self.assertIn("not PASS/FAIL", reason)

    def test_ai_at_runtime_nonzero_never_holds_aowc(self):
        card = load_example("reproduction_card.example.json")
        card["run"]["ai_at_runtime"] = 1  # schema would reject this card, but the gate check
        # itself must independently refuse to certify AOWC on such a dict, never trusting the
        # caller already ran schema validation first.
        held, reason = k.aowc_gate_check(card)
        self.assertFalse(held)
        self.assertIn("ai_at_runtime", reason)

    def test_vacuous_tolerance_never_holds_aowc(self):
        card = load_example("reproduction_card.example.json")
        card["preregistered_prediction"]["tolerance"] = "any value always passes, no tolerance"
        held, reason = k.aowc_gate_check(card)
        self.assertFalse(held)
        self.assertTrue(reason.startswith("HEURISTIC:"))

    def test_fail_result_still_holds_aowc(self):
        """P0/P23 design principle: a disclosed FAIL is exactly as strong AOWC evidence as a PASS
        -- R6 never requires the outcome to have confirmed the claim."""
        card = load_example("reproduction_card.example.json")
        card["result"]["status"] = "FAIL"
        held, reason = k.aowc_gate_check(card)
        self.assertTrue(held, reason)


# --------------------------------------------------------------------------------------------
# scripts/repro_check.py -- hashing, tolerance parsing, comparison
# --------------------------------------------------------------------------------------------

class TestHashing(unittest.TestCase):
    def test_sha256_of_file_matches_hashlib(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write("hello world")
            path = f.name
        try:
            import hashlib
            expected = hashlib.sha256(b"hello world").hexdigest()
            self.assertEqual(rc.sha256_of_file(path), expected)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_sha256_of_files_empty_is_none(self):
        self.assertIsNone(rc.sha256_of_files([]))
        self.assertIsNone(rc.sha256_of_files(None))

    def test_sha256_of_files_is_order_independent(self):
        with tempfile.TemporaryDirectory() as td:
            p1, p2 = Path(td) / "a.txt", Path(td) / "b.txt"
            p1.write_text("A")
            p2.write_text("B")
            h1 = rc.sha256_of_files([str(p1), str(p2)])
            h2 = rc.sha256_of_files([str(p2), str(p1)])
            self.assertEqual(h1, h2)

    def test_sha256_of_files_changes_with_content(self):
        with tempfile.TemporaryDirectory() as td:
            p1 = Path(td) / "a.txt"
            p1.write_text("A")
            h1 = rc.sha256_of_files([str(p1)])
            p1.write_text("A-changed")
            h2 = rc.sha256_of_files([str(p1)])
            self.assertNotEqual(h1, h2)

    def test_compute_hashes_output_ignores_a_wrappers_own_inner_self_report(self):
        """Regression, 2026-09-08: a runner that wraps an INNER pinned computation (its own
        self-reported `output_sha256` describes only the inner computation's stdout, a narrower
        byte range than THIS process's own full stdout) must never have that inner value read back
        as if it were a report about the wrapper's own stdout -- exactly the shape
        `cases/repro/run_EQ-068_higgs_pdg.py` prints, which produced a false MISMATCH on
        independent re-execution before this fix (`output_hash` never matches on ANY re-run,
        because the two values are hashes of two different byte ranges)."""
        import hashlib
        import json as _json
        wrapper_stdout = _json.dumps({
            "input_sha256": "aaaa",
            "output_sha256": "bbbb",  # hash of the INNER computation's own stdout, not this one's
            "computation_stdout": {"result": 1},
        }, indent=2, sort_keys=True)
        hashes = rc.compute_hashes(wrapper_stdout)
        # input_hash: the self-reported value is legitimately what the runner considers its own
        # input -- unaffected by this fix.
        self.assertEqual(hashes["input_hash"], "aaaa")
        # output_hash: MUST be a hash of the wrapper's own full stdout, never the inner
        # self-reported "bbbb" -- re-running the identical wrapper stdout twice must always agree
        # with a hash of that exact text, the same rule `glosa repro run`/`verify` both use.
        self.assertNotEqual(hashes["output_hash"], "bbbb")
        self.assertEqual(hashes["output_hash"], hashlib.sha256(wrapper_stdout.encode("utf-8")).hexdigest())

    def test_compute_hashes_output_prefers_a_declared_output_file_over_stdout(self):
        hashes = rc.compute_hashes('{"output_sha256": "bbbb"}', declared_output_hash="declared-hash")
        self.assertEqual(hashes["output_hash"], "declared-hash")

    def test_compute_hashes_is_stable_across_repeated_runs_of_identical_stdout(self):
        """The actual bug-fix promise: two independent executions producing byte-identical stdout
        (the paradigm case a Reproduction Card's own re-execution must satisfy) always compute the
        SAME output_hash -- unaffected by an unrelated inner self-reported key."""
        stdout_text = json.dumps({"output_sha256": "irrelevant-inner-value", "x": 1}, sort_keys=True)
        first = rc.compute_hashes(stdout_text)
        second = rc.compute_hashes(stdout_text)
        self.assertEqual(first["output_hash"], second["output_hash"])


class TestToleranceParsing(unittest.TestCase):
    def test_percent(self):
        self.assertEqual(rc.parse_tolerance("±5% of the PDG value")["kind"], "percent")
        self.assertEqual(rc.parse_tolerance("±5% of the PDG value")["pct"], 5.0)

    def test_exact_zero_discrepancy(self):
        self.assertEqual(rc.parse_tolerance("0 digit mismatch to 50 decimal places")["kind"], "exact")

    def test_exact_word_with_match_context(self):
        self.assertEqual(rc.parse_tolerance("exact integer match, 0 discrepancy")["kind"], "exact")

    def test_categorical(self):
        self.assertEqual(rc.parse_tolerance("exact categorical match (LOW/MEDIUM/HIGH -- no numeric band)")["kind"], "categorical")

    def test_unparseable(self):
        self.assertEqual(rc.parse_tolerance("whatever the reviewer feels like")["kind"], "unparseable")


class TestCompare(unittest.TestCase):
    def test_percent_pass(self):
        result = rc.compare(observed=103, reference=100, tolerance="±5% of X")
        self.assertEqual(result["status"], "PASS")

    def test_percent_fail(self):
        result = rc.compare(observed=218.005, reference=125.20, tolerance="±5% of the PDG value")
        self.assertEqual(result["status"], "FAIL")

    def test_percent_zero_reference_is_error(self):
        result = rc.compare(observed=1, reference=0, tolerance="±5% of X")
        self.assertEqual(result["status"], "ERROR")

    def test_percent_missing_reference_is_error(self):
        result = rc.compare(observed=1, reference=None, tolerance="±5% of X")
        self.assertEqual(result["status"], "ERROR")

    def test_exact_match_pass_and_fail(self):
        self.assertEqual(rc.compare(observed="12", reference="12", tolerance="exact match")["status"], "PASS")
        self.assertEqual(rc.compare(observed="12", reference="13", tolerance="exact match")["status"], "FAIL")

    def test_categorical_case_insensitive(self):
        result = rc.compare(observed="low", reference="LOW", tolerance="exact categorical match")
        self.assertEqual(result["status"], "PASS")

    def test_unparseable_tolerance_is_error_never_guessed(self):
        result = rc.compare(observed="anything", reference="anything", tolerance="whatever seems right")
        self.assertEqual(result["status"], "ERROR")


class TestToRetRows(unittest.TestCase):
    def test_coq_kernel_refused(self):
        card = load_example("reproduction_card.example.json")
        card["oracle"]["kind"] = "coq_kernel"
        with self.assertRaises(rc.ReproCheckError):
            rc.to_ret_rows(card, "claim-x")

    def test_external_oracle_produces_world_record_row(self):
        card = load_example("reproduction_card.example.json")
        rows = rc.to_ret_rows(card, "claim-x")
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["claim"], "claim-x")
        self.assertEqual(row["record_type"], "world_record")
        self.assertTrue(row["root_independent"])
        self.assertEqual(row["parent"], "-")

    def test_human_review_below_i2_refused(self):
        card = load_example("reproduction_card.example.json")
        card["oracle"]["kind"] = "human_review"
        with self.assertRaises(rc.ReproCheckError):
            rc.to_ret_rows(card, "claim-x", reviewer_independence_class="I1")

    def test_human_review_at_i2_produces_review_row(self):
        card = load_example("reproduction_card.example.json")
        card["oracle"]["kind"] = "human_review"
        rows = rc.to_ret_rows(card, "claim-x", reviewer_independence_class="I2")
        self.assertEqual(rows[0]["record_type"], "review")
        self.assertTrue(rows[0]["root_independent"])


# --------------------------------------------------------------------------------------------
# cli/glosa `repro new/run/verify/to-ret` end-to-end (subprocess, isolated tmp dir)
# --------------------------------------------------------------------------------------------

class TestCliReproEndToEnd(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.cwd = Path(self._tmp.name)
        (self.cwd / "cards").mkdir()

    def test_new_refuses_without_statement_or_tolerance(self):
        code, payload = run_cli(
            ["repro", "new", "--id", "R1", "--claim", "c", "--toledo-codes", "X/H.01.v1",
             "--oracle-kind", "independent_implementation", "--oracle-source", "s",
             "--statement", "", "--tolerance", "t", "--human-owner", "u", "--out-dir", "cards"],
            self.cwd,
        )
        self.assertEqual(code, 1)
        self.assertIn("REFUSED", payload.get("error", ""))
        self.assertFalse((self.cwd / "cards" / "R1.json").exists())

    def test_new_refuses_empty_toledo_codes_without_pending_flag(self):
        code, payload = run_cli(
            ["repro", "new", "--id", "R2", "--claim", "c",
             "--oracle-kind", "independent_implementation", "--oracle-source", "s",
             "--statement", "st", "--tolerance", "exact match", "--human-owner", "u",
             "--out-dir", "cards"],
            self.cwd,
        )
        self.assertEqual(code, 1)
        self.assertIn("pending_toledo_code", payload.get("error", ""))

    def test_new_allows_empty_toledo_codes_with_pending_flag(self):
        code, payload = run_cli(
            ["repro", "new", "--id", "R3", "--claim", "c", "--pending-toledo-code",
             "--oracle-kind", "independent_implementation", "--oracle-source", "s",
             "--statement", "st", "--tolerance", "exact match", "--human-owner", "u",
             "--out-dir", "cards"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        card_path = self.cwd / "cards" / "R3.json"
        self.assertTrue(card_path.is_file())
        card = json.loads(card_path.read_text(encoding="utf-8"))
        self.assertEqual(card["status"], "pending_toledo_code")
        self.assertEqual(card["toledo_codes"], [])
        self.assertIsNone(card["run"])
        self.assertEqual(card["result"]["status"], "PENDING")

    def test_full_lifecycle_new_run_verify_to_ret(self):
        code, _ = run_cli(
            ["repro", "new", "--id", "LIFECYCLE", "--claim", "1+3+8=12",
             "--toledo-codes", "EQ-045/H.99.v1",
             "--oracle-kind", "independent_implementation", "--oracle-source", "stdlib arithmetic",
             "--doi-or-url", "n/a", "--version", "1.0",
             "--statement", "sum equals 12", "--tolerance", "exact integer match, 0 discrepancy",
             "--human-owner", "tester", "--out-dir", "cards"],
            self.cwd,
        )
        self.assertEqual(code, 0)
        card_path = "cards/LIFECYCLE.json"

        # run
        code, payload = run_cli(
            ["repro", "run", card_path, "--command", 'python3 -c "print(1+3+8)"', "--reference", "12"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["status"], "PASS")
        card = json.loads((self.cwd / card_path).read_text(encoding="utf-8"))
        self.assertEqual(card["run"]["ai_at_runtime"], 0)
        self.assertIsNotNone(card["run"]["date"])

        # re-running the same card refuses (immutable once filled)
        code, payload = run_cli(
            ["repro", "run", card_path, "--command", 'python3 -c "print(1+3+8)"', "--reference", "12"],
            self.cwd,
        )
        self.assertEqual(code, 1)
        self.assertIn("already filled", payload.get("error", ""))

        # verify with the SAME identity as the maker refuses
        code, payload = run_cli(
            ["repro", "verify", card_path, "--reviewer-identity", "tester", "--out-dir", "reviews"],
            self.cwd,
        )
        self.assertEqual(code, 1)
        self.assertIn("REFUSED", payload.get("error", ""))

        # verify with a DIFFERENT identity succeeds and the hashes match (nothing to hash here,
        # both None==None, but the code path -- re-execution + comparison -- is exercised)
        code, payload = run_cli(
            ["repro", "verify", card_path, "--reviewer-identity", "checker1", "--out-dir", "reviews"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["hashes_match"])
        review = json.loads(Path(payload["written"]["path"]).read_text(encoding="utf-8")) if payload["written"]["path"].endswith(".json") else None
        # PyYAML may or may not be installed in the test environment -- only assert on the JSON path.
        if review is not None:
            self.assertEqual(review["role"], "SourceAuditor")
            # Regression (review journal wf_3208069c-1c1, "R5 fabricated via repro verify
            # default"): a mechanical `glosa repro verify` run with no explicit
            # --independence-class must default to I1, never the I2 that would silently satisfy
            # R5's own threshold for free -- a different --reviewer-identity STRING proves maker
            # != checker in name (P10 NC-28/29), never genuine independence (P22's own
            # "declared-independent root != independent root").
            self.assertEqual(review["independence_class"], "I1")

    def test_repro_verify_independence_class_defaults_to_i1_not_i2(self):
        """Same regression as above, isolated to the CLI flag surface: an explicit
        --independence-class I3 is honored verbatim (a human's deliberate confirmation), while
        omitting the flag never silently produces I2 or above."""
        code, _ = run_cli(
            ["repro", "new", "--id", "IC-DEFAULT", "--claim", "1+1=2",
             "--toledo-codes", "EQ-999/H.01.v1",
             "--oracle-kind", "independent_implementation", "--oracle-source", "stdlib arithmetic",
             "--doi-or-url", "n/a", "--version", "1.0",
             "--statement", "sum equals 2", "--tolerance", "exact integer match, 0 discrepancy",
             "--human-owner", "tester", "--out-dir", "cards"],
            self.cwd,
        )
        self.assertEqual(code, 0)
        card_path = "cards/IC-DEFAULT.json"
        code, _ = run_cli(
            ["repro", "run", card_path, "--command", 'python3 -c "print(1+1)"', "--reference", "2"],
            self.cwd,
        )
        self.assertEqual(code, 0)

        def _load_written(payload):
            path = self.cwd / payload["written"]["path"]
            if path.suffix != ".json":
                return None  # PyYAML-backed .yaml write -- only assert on the JSON path.
            return json.loads(path.read_text(encoding="utf-8"))

        # No --independence-class given: must default to I1.
        code, payload = run_cli(
            ["repro", "verify", card_path, "--reviewer-identity", "checker-default", "--out-dir", "reviews-default"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        review = _load_written(payload)
        if review is not None:
            self.assertEqual(review["independence_class"], "I1")

        # Explicit --independence-class I3 (a human's own deliberate confirmation) is honored.
        code, payload = run_cli(
            ["repro", "verify", card_path, "--reviewer-identity", "checker-explicit",
             "--independence-class", "I3", "--out-dir", "reviews-explicit"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        review2 = _load_written(payload)
        if review2 is not None:
            self.assertEqual(review2["independence_class"], "I3")

        # to-ret: coq_kernel oracle is refused elsewhere (TestToRetRows above); here the
        # independent_implementation oracle of this card must succeed and produce a world_record row.
        code, payload = run_cli(
            ["repro", "to-ret", card_path, "--claim", "lifecycle-claim", "--out", "ret_rows.json"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        rows = json.loads((self.cwd / "ret_rows.json").read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["record_type"], "world_record")

        # appending a second to-ret call for a different claim grows the same file, never
        # overwrites it (P22/P0's own append discipline).
        code, payload = run_cli(
            ["repro", "to-ret", card_path, "--claim", "second-claim", "--out", "ret_rows.json"],
            self.cwd,
        )
        self.assertEqual(code, 0, payload)
        rows2 = json.loads((self.cwd / "ret_rows.json").read_text(encoding="utf-8"))
        self.assertEqual(len(rows2), 2)


# --------------------------------------------------------------------------------------------
# Standard-library-only guard for the driver script (P22/P21's shared discipline; this driver
# DOES use subprocess -- that is its own declared job, unlike ret_check.py -- so this test checks
# "no THIRD-PARTY import", not "no subprocess").
# --------------------------------------------------------------------------------------------

class TestRepproCheckStdlibOnly(unittest.TestCase):
    def test_module_imports_only_stdlib(self):
        import ast
        stdlib_top_level = set(sys.stdlib_module_names) if hasattr(sys, "stdlib_module_names") else None
        source = (SCRIPTS_DIR / "repro_check.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.level == 0:
                    imported.add(node.module.split(".")[0])
        non_stdlib = {m for m in imported if m not in ("__future__",)}
        if stdlib_top_level is not None:
            non_stdlib = {m for m in non_stdlib if m not in stdlib_top_level}
        self.assertEqual(non_stdlib, set(), f"repro_check.py must import only the Python standard library; found: {non_stdlib}")


if __name__ == "__main__":
    unittest.main()
