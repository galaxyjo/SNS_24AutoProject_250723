# tests/test_audits_core.py
# ✅ pytest 기반 테스트

import os
import json
import pytest
from modules.common import audits_core


def test_parse_audit_json(tmp_path):
    file_path = tmp_path / "audit.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"issueId": "123", "url": "http://test", "type": "error"}, f)

    data = audits_core.parse_audit_json(str(file_path))
    assert data["issue_id"] == "123"
    assert data["url"] == "http://test"


def test_export_and_save_completed_file(tmp_path):
    data = {"issue_id": "123", "url": "http://test", "type": "warn"}

    audits_core.export_result(data, "audit_test.xlsx")
    audits_core.save_completed_file("audits_core.py")

    # Export 폴더가 존재해야 함
    export_dir = os.path.join(audits_core.BASE_PATH, "data", "exported_data")
    assert os.path.isdir(export_dir)


def test_ensure_path_exists(tmp_path):
    f = tmp_path / "exists.json"
    f.write_text("{}", encoding="utf-8")
    audits_core.ensure_path_exists(str(f))
    with pytest.raises(FileNotFoundError):
        audits_core.ensure_path_exists(str(f) + "_missing")
