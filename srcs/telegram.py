import requests

class TelegramSender:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message
        }
        result = requests.post(url, data=data)
        if (result.status_code == 200):
            return True
        return False
