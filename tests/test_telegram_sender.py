""" Test the TelegramSender class"""
import os
import json
from requests import HTTPError
import pytest
from srcs.telegram_sender import TelegramSender


@pytest.fixture
def hello_world_str():
    return "Hello World!"


def test_telegram_send_message_bad_config(hello_world_str):
    """Test that TelegramSender fails with bad config"""
    sender = TelegramSender("123", "123")
    with pytest.raises(HTTPError):
        sender.send_message(hello_world_str)


def test_telegram_send_message_success(hello_world_str):
    """Test that TelegramSender succeeds with good config"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    sender = TelegramSender(config["bot_token"], config["global_chat_id"])
    response = sender.send_message(hello_world_str)
    assert response["ok"] is True
    assert response["result"]["text"] == hello_world_str
