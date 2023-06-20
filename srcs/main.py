from telegramSender import TelegramSender
from gptFluffer import GPTFluffer
from foodMasterFinder import FoodMasterFinder
import datetime
import json
import os

def main():
    config = json.loads(os.environ["GSTALDERCONFIG"])

    foodMasterFinder = FoodMasterFinder(
        config["flatmates"], 
        datetime.date.today() + datetime.timedelta(days=1)
        )
    introductionText = foodMasterFinder.getIntroductionText()

    fluffer = GPTFluffer(config["open_ai_key"])    
    message = fluffer.fluff(introductionText) 

    sender = TelegramSender(config["bot_token"], config["chat_id"])
    sender.send_message(message)
    return 0

if __name__ == "__main__": 
    main()