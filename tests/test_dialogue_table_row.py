"""tests/test_dialogue_table_row.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers `lrs.dialogue-table-claim-type-column` (design/SESSION_ARCH_v0.4_SPEC.md §10.1, build_now):
the `defeater_class` + `legitimate_defeater` columns added to `schema/dialogue_table_row.schema.
json`, matching the already-shipped `templates/knowledge/dialogue_table.md` columns. Both fields
are deliberately SCHEMA-OPTIONAL (additive), not `required` -- the template documents the
stance-without-defeater-columns check as a LINT (`INCOMPLETE: ...`), not a hard schema validator,
mechanically enforced instead by `cli/glosa`'s `_dialogue_row_incomplete`/`glosa lit table`
(`rows_incomplete_defeater`) -- see `tests/test_install.py::DialogueTableDefeaterColumnsTest` for
that enforcement path. This file only covers the schema shape (the enum values, and that the
fields are additive/backward-compatible), not the lint itself.

Deliberately does NOT add or test a `defeater_status` field on this row: `templates/knowledge/
dialogue_table.md`'s own `lrs.defeater-defeated-status-field` TODO note states that fact lives on
`schema/claim_card.schema.json`'s `provenance_dag.defeater_log` (one-fact-one-home), not as a
duplicate status column here -- see `tests/test_kernel.py`'s `SessionArchV04Test` /
rule29-rule30 coverage, and `tests/test_defeater_status_warning.py`, for that field instead.
"""

import copy
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "kernel"))

import glosa_kernel as k  # noqa: E402

EXAMPLES_DIR = REPO_ROOT / "schema" / "examples"
SCHEMA_NAME = "dialogue_table_row.schema.json"


def load_example():
    return json.loads((EXAMPLES_DIR / "dialogue_table_row.example.json").read_text(encoding="utf-8"))


def validate(instance):
    errors, used_fallback = k._schema_validate(instance, SCHEMA_NAME)
    assert not used_fallback, "jsonschema RefResolver unavailable -- install jsonschema to run this test for real"
    return errors


class DialogueTableRowDefeaterColumnsTest(unittest.TestCase):
    def test_shipped_example_with_defeater_columns_passes(self):
        row = load_example()
        self.assertEqual(validate(row), [])

    def test_stance_yes_missing_defeater_class_still_validates_schema_level(self):
        # Deliberately additive/optional at the schema level -- the INCOMPLETE check is a
        # cli/glosa lint (rows_incomplete_defeater), not a schema `required`. See module docstring.
        row = copy.deepcopy(load_example())
        del row["defeater_class"]
        self.assertEqual(validate(row), [])

    def test_stance_yes_missing_legitimate_defeater_still_validates_schema_level(self):
        row = copy.deepcopy(load_example())
        del row["legitimate_defeater"]
        self.assertEqual(validate(row), [])

    def test_orthogonal_stance_without_defeater_columns_passes(self):
        row = copy.deepcopy(load_example())
        row["stance"] = "ORTHOGONAL"
        del row["defeater_class"]
        del row["legitimate_defeater"]
        self.assertEqual(validate(row), [])

    def test_undetermined_stance_without_defeater_columns_passes(self):
        row = copy.deepcopy(load_example())
        row["stance"] = "UNDETERMINED"
        row["verified"] = {"metadata_verified": True, "claim_match_verified": False}
        del row["defeater_class"]
        del row["legitimate_defeater"]
        self.assertEqual(validate(row), [])

    def test_defeater_class_enum_is_the_five_way_lowercase_taxonomy(self):
        row = copy.deepcopy(load_example())
        row["defeater_class"] = "EMPIRICAL"  # wrong case -- schema enum is lowercase, distinct
        # namespace from claim_card.schema.json's uppercase five_questions.tested.defeater_class
        self.assertTrue(validate(row))


if __name__ == "__main__":
    unittest.main()
