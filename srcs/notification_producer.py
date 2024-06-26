""" NotificationProducer class"""
import datetime
from .message_formater import MessageFormater
from .telegram_sender import TelegramSender



class NotificationProducer:
    """Parent class to create telegram notifications."""

    def __init__(self, food_master_finder, trash_schedule_grabber, config):
        self.food_master_finder = food_master_finder
        self.message_formater = MessageFormater(
            food_master_finder.get_current()["name"]
        )
        self.trash_schedule_grabber = trash_schedule_grabber
        self.config = config

    def send_food_master_change(self) -> dict:
        """Sends a message to the telegram chat to announce a new food master."""
        previous_master = self.food_master_finder.get_previous()
        introduction_text = self.message_formater.get_role_update_text(
            previous_master["name"]
        )

        fluffed_introduction_text = introduction_text

        sender = TelegramSender(self.config["bot_token"], self.config["global_chat_id"])
        return sender.send_message(fluffed_introduction_text)

    def send_weekly_schedule(self) -> dict:
        """Sends a message to the telegram chat with the weekly trash schedule."""
        schedule = self.trash_schedule_grabber.get_schedule(
            from_date=datetime.datetime.today(),
            until_date=datetime.datetime.today() + datetime.timedelta(days=7),
        )
        weekly_schedule_text = self.message_formater.get_weekly_schedule_text(schedule)

        food_master_chat_sender = TelegramSender(
            token=self.config["bot_token"],
            chat_id=self.food_master_finder.get_current()["chat_id"],
        )
        return food_master_chat_sender.send_message(weekly_schedule_text)

    def send_daily_schedule(self) -> dict:
        """Sends a message to the telegram chat with the trashes of the day to take out."""
        schedule = self.trash_schedule_grabber.get_schedule(
            from_date=datetime.datetime.today()
        )

        # checks if we found any trashes for tomorrow
        if len(schedule) == 0:
            trashes = []
        else:
            trashes = list(schedule.values())[0]

        daily_schedule_text = self.message_formater.get_daily_update_text(
            trash_list=trashes
        )

        food_master_chat_sender = TelegramSender(
            token=self.config["bot_token"],
            chat_id=self.food_master_finder.get_current()["chat_id"],
        )
        return food_master_chat_sender.send_message(daily_schedule_text)
