import subprocess
from typing import List, Tuple

def run_git(cmd: List[str], cwd: str = ".") -> Tuple[str, str]:
    """Runs a git command and returns stdout, stderr."""
    result = subprocess.run(
        ["git"] + cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False
    )
    return result.stdout, result.stderr
