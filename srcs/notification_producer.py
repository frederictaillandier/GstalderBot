""" NotificationProducer class"""
import datetime
import sys
import os
sys.path.append(os.getcwd())
from srcs.message_formater import MessageFormater
from srcs.telegram_sender import TelegramSender
from srcs.gpt_fluffer import GPTFluffer

class NotificationProducer:
    """ Parent class to create telegram notifications. """
    def __init__(self, food_master_finder, trash_schedule_grabber, config):
        self.food_master_finder = food_master_finder
        self.message_formater = MessageFormater(
            food_master_finder.get_current()['name']
            )
        self.trash_schedule_grabber = trash_schedule_grabber
        self.config = config

    def send_food_master_change(self):
        """ Sends a message to the telegram chat to announce a new food master. """
        previous_master = self.food_master_finder.get_previous()
        introduction_text = self.message_formater.get_role_update_text(previous_master['name'])

        fluffer = GPTFluffer(self.config["open_ai_key"])
        fluffed_introduction_text = fluffer.fluff(introduction_text)

        sender = TelegramSender(
            self.config["bot_token"],
            self.config["global_chat_id"]
        )
        return sender.send_message(fluffed_introduction_text)

    def send_weekly_schedule(self):
        """ Sends a message to the telegram chat with the weekly trash schedule. """
        schedule = self.trash_schedule_grabber.get_schedule(
            datetime.datetime.today() + datetime.timedelta(days=1),
            datetime.datetime.today() + datetime.timedelta(days=8)
            )
        weekly_schedule_text = self.message_formater.get_weekly_schedule_text(schedule)

        food_master_chat_sender = TelegramSender(
            self.config["bot_token"],
            self.food_master_finder.get_current()["chat_id"]
            )
        return food_master_chat_sender.send_message(weekly_schedule_text)

    def send_daily_schedule(self):
        """ Sends a message to the telegram chat with the trashes of the day to take out. """
        schedule = self.trash_schedule_grabber.get_schedule(
            datetime.datetime.today()
            )
        daily_schedule_text = self.message_formater.get_daily_update_text(schedule)

        food_master_chat_sender = TelegramSender(
            self.config["bot_token"],
            self.food_master_finder.get_current()["chat_id"]
            )
        return food_master_chat_sender.send_message(daily_schedule_text)
