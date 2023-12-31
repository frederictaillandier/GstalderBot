"""Telegram Sender Module to send messages to a telegram chat."""
import requests


class TelegramSender:
    """Class to send messages to a telegram chat."""

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, message: str) -> dict:
        """Sends a message to the telegram chat."""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message}
        result = requests.post(url, data=data, timeout=5)
        result.raise_for_status()
        return result.json()
