# tests/test_uploader_instagram.py

import os
import asyncio
import pytest
from modules.sns import uploader_instagram


def test_uploader_instagram_exists():
    file_path = os.path.join("modules", "sns", "uploader_instagram.py")
    assert os.path.exists(file_path), "uploader_instagram.py 파일이 존재하지 않습니다."


def test_uploader_instagram_import():
    assert hasattr(uploader_instagram, "upload_post")
    assert hasattr(uploader_instagram, "upload_story")


@pytest.mark.asyncio
async def test_upload_post_invalid_file():
    result = await uploader_instagram.upload_post("없는파일.jpg", caption="Test")
    assert result is False


@pytest.mark.asyncio
async def test_upload_story_invalid_file():
    result = await uploader_instagram.upload_story("없는파일.png")
    assert result is False


@pytest.mark.asyncio
async def test_upload_post_valid(tmp_path):
    test_file = tmp_path / "test.jpg"
    test_file.write_text("fake content")
    result = await uploader_instagram.upload_post(str(test_file), caption="hello")
    assert result is True


@pytest.mark.asyncio
async def test_upload_story_valid(tmp_path):
    test_file = tmp_path / "story.mp4"
    test_file.write_text("video content")
    result = await uploader_instagram.upload_story(str(test_file))
    assert result is True


# 예외 유발 테스트


@pytest.mark.asyncio
async def test_upload_post_raises(tmp_path, monkeypatch):
    test_file = tmp_path / "fail.jpg"
    test_file.write_text("data")

    async def fake_sleep_error(_):
        raise RuntimeError("강제 예외")

    monkeypatch.setattr(uploader_instagram, "asyncio", asyncio)
    monkeypatch.setattr(uploader_instagram.asyncio, "sleep", fake_sleep_error)

    result = await uploader_instagram.upload_post(str(test_file), caption="에러테스트")
    assert result is False


@pytest.mark.asyncio
async def test_upload_story_raises(tmp_path, monkeypatch):
    test_file = tmp_path / "fail.mp4"
    test_file.write_text("data")

    async def fake_sleep_error(_):
        raise RuntimeError("강제 예외")

    monkeypatch.setattr(uploader_instagram, "asyncio", asyncio)
    monkeypatch.setattr(uploader_instagram.asyncio, "sleep", fake_sleep_error)

    result = await uploader_instagram.upload_story(str(test_file))
    assert result is False
