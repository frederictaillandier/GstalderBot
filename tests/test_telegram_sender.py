""" Test the TelegramSender class"""
import os
import json
from requests import HTTPError
import pytest
from srcs.telegram_sender import TelegramSender


def test_telegram_send_message_bad_config():
    """Test that TelegramSender fails with bad config"""
    sender = TelegramSender("123", "123")
    with pytest.raises(HTTPError):
        sender.send_message("Hello World!")


def test_telegram_send_message_success():
    """Test that TelegramSender succeeds with good config"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    sender = TelegramSender(config["bot_token"], config["global_chat_id"])
    response = sender.send_message("Hello World!")
    assert response["ok"] is True
    assert response["result"]["text"] == "Hello World!"
