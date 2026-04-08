import os
from slopguard.config import SlopGuardConfig


def test_default_config():
    conf = SlopGuardConfig()
    assert conf.thresholds.fail_score == 80
    assert conf.thresholds.warn_score == 50
    assert conf.baseline.enabled is True


def test_config_save_load(tmp_path):
    conf_path = os.path.join(tmp_path, ".slopguard.yml")
    conf = SlopGuardConfig()
    conf.thresholds.fail_score = 90
    conf.save(conf_path)

    loaded = SlopGuardConfig.load(conf_path)
    assert loaded.thresholds.fail_score == 90
