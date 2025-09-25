# tests/test_scripts_core.py
import os
import pytest
import scripts.generate_release as gr
import scripts.auto_git_webhook as agw
import scripts.install_package as ip
import scripts.create_release_zip as crz

def test_generate_release_info():
    path = gr.generate_release_info()
    assert os.path.exists(path)

def test_generate_qa_review():
    path = gr.generate_qa_review()
    assert os.path.exists(path)

def test_generate_operational_plan():
    path = gr.generate_operational_plan()
    assert os.path.exists(path)

def test_generate_log_statistics():
    gr.generate_log_statistics()

def test_auto_git_webhook(monkeypatch):
    monkeypatch.setattr("requests.post", lambda url, json: type("obj", (object,), {"status_code":200})())
    agw.send_git_webhook()

def test_create_release_zip(tmp_path, monkeypatch):
    # 더미 파일 생성
    base_dir = "C:\\SNS_24AutoProject"
    os.makedirs(base_dir, exist_ok=True)
    dummy_main = os.path.join(base_dir, "main.py")
    dummy_ps1 = os.path.join(base_dir, "insert_logtrace_auto.ps1")
    with open(dummy_main, "w", encoding="utf-8") as f:
        f.write("print('hello')")
    with open(dummy_ps1, "w", encoding="utf-8") as f:
        f.write("echo hello")
    crz.create_release_zip()
    assert os.path.exists("C:\\backup_Release.zip")
