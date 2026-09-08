"""tests/test_zenodo_remove_relation.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers `scripts/zenodo_remove_relation.py`'s pure function `compute_removal(related_identifiers,
target, relation)` only -- no network call, no token. Exercises the guarantee this task depended
on: removing a wrong `isPartOf` relation from a Zenodo record's related_identifiers list must drop
ONLY the exact (identifier, relation) pair and leave every other entry byte-identical, in order
(founder ruling BBL-2026-09-08-243, item 1: removing the islam/se hub isPartOf relations wrongly
carried by concept 22302409/22301885 while keeping their genuine aihp/ai/ep relations untouched).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from zenodo_remove_relation import compute_removal  # noqa: E402


class TestComputeRemoval(unittest.TestCase):
    def test_removes_only_exact_match(self):
        rel = [
            {'identifier': '10.5281/zenodo.111', 'relation': 'references', 'resource_type': 'publication-preprint', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.222', 'relation': 'isPartOf', 'resource_type': 'publication-other', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.333', 'relation': 'isPartOf', 'resource_type': 'publication-other', 'scheme': 'doi'},
        ]
        kept, removed = compute_removal(rel, '10.5281/zenodo.222', 'isPartOf')
        self.assertEqual(removed, [rel[1]])
        self.assertEqual(kept, [rel[0], rel[2]])

    def test_kept_entries_are_byte_identical_and_order_preserved(self):
        rel = [
            {'identifier': '10.5281/zenodo.aaa', 'relation': 'references', 'resource_type': 'publication-preprint', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.bbb', 'relation': 'isPartOf', 'resource_type': 'publication-other', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.ccc', 'relation': 'isSupplementTo', 'resource_type': 'publication-preprint', 'scheme': 'doi'},
        ]
        kept, removed = compute_removal(rel, '10.5281/zenodo.bbb', 'isPartOf')
        self.assertEqual(kept, [rel[0], rel[2]])
        for k in kept:
            self.assertIn(k, rel)

    def test_same_identifier_different_relation_is_not_removed(self):
        # a record can carry the same DOI under two different relations (e.g. isPartOf a hub AND
        # references it as an anchor is not realistic, but the function must key on the PAIR, not
        # the identifier alone).
        rel = [
            {'identifier': '10.5281/zenodo.999', 'relation': 'references', 'resource_type': 'publication-preprint', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.999', 'relation': 'isPartOf', 'resource_type': 'publication-other', 'scheme': 'doi'},
        ]
        kept, removed = compute_removal(rel, '10.5281/zenodo.999', 'isPartOf')
        self.assertEqual(removed, [rel[1]])
        self.assertEqual(kept, [rel[0]])

    def test_no_match_returns_everything_kept_nothing_removed(self):
        rel = [
            {'identifier': '10.5281/zenodo.111', 'relation': 'references', 'resource_type': 'publication-preprint', 'scheme': 'doi'},
        ]
        kept, removed = compute_removal(rel, '10.5281/zenodo.does-not-exist', 'isPartOf')
        self.assertEqual(kept, rel)
        self.assertEqual(removed, [])

    def test_empty_input(self):
        kept, removed = compute_removal([], '10.5281/zenodo.222', 'isPartOf')
        self.assertEqual(kept, [])
        self.assertEqual(removed, [])

    def test_removes_all_matching_duplicates(self):
        # defensive: if a record ever carried the wrong relation twice, both copies go, not just one.
        rel = [
            {'identifier': '10.5281/zenodo.222', 'relation': 'isPartOf', 'resource_type': 'publication-other', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.222', 'relation': 'isPartOf', 'resource_type': 'publication-other', 'scheme': 'doi'},
            {'identifier': '10.5281/zenodo.333', 'relation': 'references', 'resource_type': 'publication-preprint', 'scheme': 'doi'},
        ]
        kept, removed = compute_removal(rel, '10.5281/zenodo.222', 'isPartOf')
        self.assertEqual(len(removed), 2)
        self.assertEqual(kept, [rel[2]])


if __name__ == '__main__':
    unittest.main()
