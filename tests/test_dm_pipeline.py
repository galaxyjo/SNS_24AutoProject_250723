import pytest
from modules.dm.queue import DMQueue
from modules.dm.bot_comment import BotCommentManager


@pytest.fixture
def mock_queue(monkeypatch):
    dummy_data = [{"id": "123", "text": "hello"}, {"id": "456", "text": "scam text"}]
    monkeypatch.setattr(DMQueue, "consume", lambda self: dummy_data)
    return DMQueue()


@pytest.fixture
def mock_bot(monkeypatch):
    monkeypatch.setattr(BotCommentManager, "send_comment", lambda self, item: True)
    return BotCommentManager()


def test_pipeline_comment_sent(mock_queue, mock_bot):
    data = mock_queue.consume()
    results = [mock_bot.send_comment(item) for item in data]
    assert all(results)
    assert len(results) == 2
