from telegram_sender import TelegramSender
from gpt_fluffer import GPTFluffer
from food_master_finder import FoodMasterFinder
import datetime
import json
import os

def main():
    config = json.loads(os.environ["GSTALDERCONFIG"])

    food_master_finder = FoodMasterFinder(
        config["flatmates"], 
        datetime.date.today() + datetime.timedelta(days=1)
        )
    introduction_text = food_master_finder.get_introduction_text()

    fluffer = GPTFluffer(config["open_ai_key"])    
    message = fluffer.fluff(introduction_text) 

    sender = TelegramSender(config["bot_token"], config["chat_id"])
    sender.send_message(message)
    return 0

if __name__ == "__main__": 
    main()