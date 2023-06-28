"""Telegram Sender Module to send messages to a telegram chat."""
import requests

class TelegramSender:
    """Class to send messages to a telegram chat."""
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, message):
        """Sends a message to the telegram chat."""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message
        }
        result = requests.post(url, data=data, timeout=5)
        if result.status_code == 200:
            return True
        return False
