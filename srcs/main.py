from telegram import TelegramSender
import json
import os

def main():
    config = json.loads(os.environ["GSTALDERCONFIG"])
    sender = TelegramSender(config["bot_token"], config["chat_id"])
    sender.send_message("Hello World!")
    return 0

if __name__ == "__main__": 
    main()
