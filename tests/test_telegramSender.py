import sys
sys.path.append('../srcs/')
import pytest
import os, json
from srcs.telegramSender import TelegramSender

def test_telegram_init():
    with pytest.raises(Exception) as e_info:
        TelegramSender()

def test_telegram_send_message_bad_config():
    sender = TelegramSender("123", "123")
    assert sender.send_message("Hello World!") == False

def test_telegram_send_message_success():
    config = json.loads(os.environ["GSTALDERCONFIG"])
    sender = TelegramSender(config["bot_token"], config["chat_id"])
    assert sender.send_message("Hello World!") == True
