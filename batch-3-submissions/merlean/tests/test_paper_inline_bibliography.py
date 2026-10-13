"""Inline reader bibliography retains independent export/render evidence."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from paper_writing_codex.cli import _inline_bibliography_audit
from paper_writing_codex.tex_inventory import inventory_tex
from paper_writing_codex.versioning import sha256_file


class InlineBibliographyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paper = self.root / 'paper.tex'
        self.rendered = r'\bibitem{Author2026} A. Author, A useful result (2026).'
        self.paper.write_text(r'\documentclass{article}\begin{document}'
                             r'\cite{Author2026}\begin{thebibliography}{1}'
                             + self.rendered + r'\end{thebibliography}\end{document}')
        self.state = {'output': str(self.paper), 'work_dir': str(self.root)}
        self.inventory = inventory_tex(self.paper)
        self.export = '@article{Author2026, title={A useful result}, author={A. Author}, year={2026}}'
        self.entry = {'citation_key': 'Author2026', 'rendered_entry': self.rendered,
                      'bibtex_sha256': hashlib.sha256(self.export.encode()).hexdigest()}
        self.audit = {'reviewer_id': 'independent-source-reader', 'writer_ids': ['writer'],
                      'verdict': 'PASS', 'unresolved_findings': [],
                      'candidate_source_tree_sha256': self.inventory['source_tree_sha256'],
                      'bibliography_entries': [{'citation_key': 'Author2026',
                          'bibtex_sha256': self.entry['bibtex_sha256'],
                          'rendered_entry_sha256': hashlib.sha256(self.rendered.encode()).hexdigest(),
                          'findings': 'The exact rendered authors, title and year agree with the inspected export.'}]}

    def check(self):
        path = self.root / 'source-audit.json'
        path.write_text(json.dumps(self.audit))
        self.entry['rendered_bibliography_audit'] = {'path': str(path), 'sha256': sha256_file(path)}
        _inline_bibliography_audit(self.state, self.inventory, self.entry, self.export,
                                   self.paper.read_text(), self.paper)

    def test_inline_entry_does_not_need_raw_bibtex_in_paper(self):
        self.assertNotIn(self.export, self.paper.read_text())
        self.check()

    def test_stale_or_nonindependent_or_unresolved_audit_rejected(self):
        for key, value in [('reviewer_id', 'writer'), ('verdict', 'FAIL'),
                           ('unresolved_findings', ['Wrong authors']),
                           ('candidate_source_tree_sha256', '0' * 64)]:
            with self.subTest(key=key):
                old = self.audit[key]
                self.audit[key] = value
                with self.assertRaises(ValueError): self.check()
                self.audit[key] = old

    def test_invented_or_altered_entry_rejected(self):
        self.entry['rendered_entry'] = self.rendered + ' An invented claim.'
        with self.assertRaises(ValueError): self.check()

    def test_wrong_export_binding_rejected(self):
        self.audit['bibliography_entries'][0]['bibtex_sha256'] = '0' * 64
        with self.assertRaises(ValueError): self.check()


if __name__ == '__main__':
    unittest.main()
