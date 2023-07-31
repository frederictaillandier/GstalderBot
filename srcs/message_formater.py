"""Module providing the MessageFormater class to format the messages to be sent."""
import calendar
from enum import Enum

WASTE_TYPE_DESCRIPTION = (
    "We recycle",
    "Normal",
    "Bio",
    "Carboard",
    "Paper",
    "Unknown",
    "Unknown2",
    "Hazard",
)


def format_trash_list(trash_list: list[int]) -> str:
    """Returns a string with the trash types separated by commas and the last one by an 'and'.
    Example: ['Normal', 'Bio', 'Carboard'] -> 'Normal, Bio and Carboard'"""
    if len(trash_list) == 1:
        return WASTE_TYPE_DESCRIPTION[trash_list[0]]
    return f"{WASTE_TYPE_DESCRIPTION[trash_list[0]]} and {format_trash_list(trash_list=trash_list[1:])}"


class MessageFormater:
    """Formats the messages to be sent."""

    def __init__(self, food_master):
        self.food_master = food_master

    def get_role_update_text(self, ex_food_master: str) -> str:
        """Returns the text to be sent to the global
        chat when the food master changes."""
        return f"""{ex_food_master} is no more the food master. {self.food_master} is the new food master.\n\n"""

    def get_daily_update_text(self, trash_list: list[int]) -> str:
        """Returns the text to be send to the food master every day for the tasks of the day.
        Example: trash_list = [1, 2] -> 'Normal and Bio'
        """
        if len(trash_list) == 0:
            return f"Hi { self.food_master }! No trash pickup for tomorrow, have a nice evening!\n\n"
        message_builder: list = []
        message_builder.append(f"Hi { self.food_master }! ")
        message_builder.append(
            f"Don't forget to take out the {format_trash_list(trash_list)} before 7am tomorrow.\n"
        )
        # We-recycle bag check
        if 0 in trash_list:
            message_builder.append("Do we still have enough we-recycle bags ?\n")
            message_builder.append(
                "If not, can you order some new ? By adding a sticker on the last bag ?\n"
            )
        message_builder.append("Have a nice evening.")
        return "".join(message_builder)

    def get_weekly_schedule_text(self, schedule: dict) -> str:
        """Returns the text to be send to the food master every week for the tasks of the week.
        Example: schedule = {
            datetime.date(2021, 6, 1): [1, 2],
            datetime.date(2021, 6, 2): [0, 3]
        }"""
        message_builder: list = []
        message_builder.append(
            f"Hello {self.food_master},\nfor this week you need to put these trashes in front the house before 7:00am:\n"
        )
        for date in schedule:
            message_builder.append(
                f"The {format_trash_list(schedule[date])} on {calendar.day_name[date.weekday()]}.\n"
            )
        message_builder.append("Thank you !\n")
        return "".join(message_builder)
