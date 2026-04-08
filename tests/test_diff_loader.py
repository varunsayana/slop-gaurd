from slopguard.engine.diff_loader import DiffLoader

def test_diff_loader_init():
    loader = DiffLoader(".")
    assert loader.repo_path == "."
