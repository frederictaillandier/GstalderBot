from telegram import TelegramSender
from gpt import GPTFluffer
import json
import os

def main():
    config = json.loads(os.environ["GSTALDERCONFIG"])
    sender = TelegramSender(config["bot_token"], config["chat_id"])
    fluffer = GPTFluffer(config["open_ai_key"])    

    message = fluffer.fluff("Hello World!") 
    sender.send_message(message)
    return 0

if __name__ == "__main__": 
    main()