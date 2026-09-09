"""tests/test_zenodo_cluster_tag_guard.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Guards the 2026-09-08 incident (registry/ZENODO_HUB_PLAN.md): running `zenodo_cluster.py
hubs-refresh` right after a bare `fetch` (no `tag` in between) briefly wiped hasPart membership
live on Zenodo, because `members_of()` (called by `cmd_hubs_refresh`) depends on `cluster`/`tags`
fields that only `cmd_tag` sets on each record. This test exercises the guard function
`check_tag_ran` added to close that hole -- no network call, no token.
"""

import json
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))

import zenodo_cluster as zc  # noqa: E402


class TestTagGuard(unittest.TestCase):
    def setUp(self):
        self._orig_recs = zc.RECS
        self._orig_tag_state = zc.TAG_STATE
        self.tmp = REPO / '_tmp_test_zenodo_cluster_tag_guard'
        self.tmp.mkdir(exist_ok=True)
        zc.RECS = str(self.tmp / 'zenodo_all_records.json')
        zc.TAG_STATE = str(self.tmp / 'zenodo_tag_state.json')

    def tearDown(self):
        zc.RECS = self._orig_recs
        zc.TAG_STATE = self._orig_tag_state
        for f in self.tmp.glob('*'):
            f.unlink()
        self.tmp.rmdir()

    def _write_recs(self, obj):
        json.dump(obj, open(zc.RECS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    def test_refuses_when_no_recs_file(self):
        with self.assertRaises(SystemExit) as ctx:
            zc.check_tag_ran(argv=['zenodo_cluster.py', 'hubs-refresh'])
        self.assertEqual(ctx.exception.code, 2)

    def test_refuses_bare_fetch_without_tag(self):
        # simulates: fetch just ran (RECS exists, untagged), no TAG_STATE recorded yet
        self._write_recs([{'id': 1, 'doi': '10.5281/zenodo.1', 'title': 'x'}])
        with self.assertRaises(SystemExit) as ctx:
            zc.check_tag_ran(argv=['zenodo_cluster.py', 'hubs-refresh'])
        self.assertEqual(ctx.exception.code, 2)

    def test_refuses_when_fetch_ran_again_after_tag(self):
        # tag ran and recorded a hash matching the tagged content...
        self._write_recs([{'id': 1, 'doi': '10.5281/zenodo.1', 'title': 'x', 'cluster': 'ep', 'tags': []}])
        zc.save(zc.TAG_STATE, {'recs_sha256': zc._file_sha256(zc.RECS), 'tagged_at': 'then'})
        # ...but a bare `fetch` ran again afterward, overwriting RECS with fresh untagged content
        self._write_recs([{'id': 1, 'doi': '10.5281/zenodo.1', 'title': 'x'}])
        with self.assertRaises(SystemExit) as ctx:
            zc.check_tag_ran(argv=['zenodo_cluster.py', 'hubs-refresh'])
        self.assertEqual(ctx.exception.code, 2)

    def test_passes_when_tag_ran_on_current_recs(self):
        self._write_recs([{'id': 1, 'doi': '10.5281/zenodo.1', 'title': 'x', 'cluster': 'ep', 'tags': []}])
        zc.save(zc.TAG_STATE, {'recs_sha256': zc._file_sha256(zc.RECS), 'tagged_at': 'now'})
        zc.check_tag_ran(argv=['zenodo_cluster.py', 'hubs-refresh'])  # must not raise/exit

    def test_override_flag_bypasses_check(self):
        # no RECS, no TAG_STATE at all -- override must still bypass (last-resort escape hatch)
        zc.check_tag_ran(argv=['zenodo_cluster.py', 'hubs-refresh', '--i-confirm-tag-ran'])

    def test_cmd_tag_writes_matching_tag_state(self):
        self._write_recs([{'id': 1, 'doi': '10.5281/zenodo.1', 'title': 'quantum gravity', 'date': '2026-01-01', 'kw': [], 'desc': ''}])
        zc.cmd_tag()
        state = json.load(open(zc.TAG_STATE, encoding='utf-8'))
        self.assertEqual(state['recs_sha256'], zc._file_sha256(zc.RECS))
        # guard now passes on the file cmd_tag itself just wrote
        zc.check_tag_ran(argv=['zenodo_cluster.py', 'hubs-refresh'])


if __name__ == '__main__':
    unittest.main()
