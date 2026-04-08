"""
Diff Loader using Git & Unidiff.
"""

from typing import List, Optional
import unidiff
import os
from slopguard.utils.subprocess import run_git


class DiffLoader:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def get_diff_from_refs(
        self, base_ref: str, head_ref: str
    ) -> Optional[unidiff.PatchSet]:
        """Gets diff between two git refs."""
        stdout, stderr = run_git(["diff", base_ref, head_ref], cwd=self.repo_path)
        if not stdout:
            return None
        return unidiff.PatchSet(stdout)

    def get_diff_staged(self) -> Optional[unidiff.PatchSet]:
        """Gets staged changes."""
        stdout, stderr = run_git(["diff", "--cached"], cwd=self.repo_path)
        if not stdout:
            return None
        return unidiff.PatchSet(stdout)

    def load_patch_file(self, patch_path: str) -> Optional[unidiff.PatchSet]:
        """Loads diff from a raw patch file."""
        if not os.path.exists(patch_path):
            return None
        with open(patch_path, "r", encoding="utf-8") as f:
            return unidiff.PatchSet(f.read())

    def construct_file_diff(self, file_path: str) -> Optional[unidiff.PatchSet]:
        """Gets uncommitted diff for a single file."""
        stdout, stderr = run_git(["diff", file_path], cwd=self.repo_path)
        if not stdout:
            return None
        return unidiff.PatchSet(stdout)
