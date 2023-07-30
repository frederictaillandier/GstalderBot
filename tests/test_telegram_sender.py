""" Test the TelegramSender class"""
import os
import json
from srcs.telegram_sender import TelegramSender


def test_telegram_send_message_bad_config():
    """Test that TelegramSender fails with bad config"""
    sender = TelegramSender("123", "123")
    assert not sender.send_message("Hello World!")


def test_telegram_send_message_success():
    """Test that TelegramSender succeeds with good config"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    sender = TelegramSender(config["bot_token"], config["global_chat_id"])
    assert sender.send_message("Hello World!")
