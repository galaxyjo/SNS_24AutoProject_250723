import pytest
from modules.dm.bot_comment import Comment, BotCommentManager, handle_comment


def test_generate_reply_empty():
    mgr = BotCommentManager()
    comment = Comment(user_id="u1", text="")
    assert mgr.generate_reply(comment) == "[BOT] 안녕하세요! 무엇을 도와드릴까요?"


def test_generate_reply_help_english():
    mgr = BotCommentManager()
    comment = Comment(user_id="u2", text="help me")
    assert mgr.generate_reply(comment) == "[BOT] 도움이 필요하시면 키워드 알려주세요."


def test_generate_reply_help_korean():
    mgr = BotCommentManager()
    comment = Comment(user_id="u3", text="도움 주세요")
    assert mgr.generate_reply(comment) == "[BOT] 도움이 필요하시면 키워드 알려주세요."


def test_generate_reply_normal_text():
    mgr = BotCommentManager()
    comment = Comment(user_id="u4", text="문의드립니다")
    assert mgr.generate_reply(comment) == "[BOT] 문의드립니다 감사합니다!"


def test_handle_comment_wrapper():
    reply = handle_comment("도움이 필요해요", user_id="u5", post_id="p1")
    assert reply == "[BOT] 도움이 필요하시면 키워드 알려주세요."
