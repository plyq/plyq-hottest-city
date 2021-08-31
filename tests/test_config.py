import pytest

import hottest.config as hcfg


def test_get1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TESTENVVAR", "TESTENVVAL")
    assert hcfg.get("TESTENVVAR") == "TESTENVVAL"


def test_get_root_dir1() -> None:
    assert "hottest" in hcfg.get_root_dir()
