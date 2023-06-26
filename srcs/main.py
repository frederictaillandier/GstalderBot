from telegram_sender import TelegramSender
from gpt_fluffer import GPTFluffer
from food_master_finder import FoodMasterFinder
from trash_schedule_grabber import TrashScheduleGrabber
import message_formater
import datetime
import json
import os

def main():
    # get config and builders
    config = json.loads(os.environ["GSTALDERCONFIG"])
    trash_schedule_grabber = TrashScheduleGrabber()

    # get food masters
    food_master_finder = FoodMasterFinder(
        config["flatmates"], 
        datetime.date.today() + datetime.timedelta(days=1)
        )
    master = food_master_finder.get_current()
    previous_master = food_master_finder.get_previous()
    schedule = trash_schedule_grabber.get_schedule(datetime.datetime.today() + datetime.timedelta(days=1), datetime.datetime.today() + datetime.timedelta(days=8))

    text_formater = message_formater.MessageFormater(master['name'])

    # build and send role update message
    global_chat_sender = TelegramSender(config["bot_token"], config["global_chat_id"])

    introduction_text = text_formater.get_role_update_text(previous_master['name'])
    fluffer = GPTFluffer(config["open_ai_key"])    
    message = fluffer.fluff(introduction_text) 
    global_chat_sender.send_message(message)

    # build and send weelkly schedule message
    weekly_schedule_text = text_formater.get_weekly_schedule_text(schedule)
    food_master_chat_sender = TelegramSender(config["bot_token"], master["chat_id"])
    food_master_chat_sender.send_message(weekly_schedule_text)

    return 0

if __name__ == "__main__": 
    main()