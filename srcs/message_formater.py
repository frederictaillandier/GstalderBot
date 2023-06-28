"""Module providing the MessageFormater class to format the messages to be sent."""
import calendar

# Matches the trash type text and indices
waste_type = ["We recycle", "Normal", "Bio", "Carboard", "Paper", "Unknown", "Unknown2", "Hazard"]

def format_trash_list(trash_list):
    """Returns a string with the trash types separated by commas and the last one by an 'and'.
    Example: ['Normal', 'Bio', 'Carboard'] -> 'Normal, Bio and Carboard'"""
    if len(trash_list) == 1:
        return waste_type[trash_list[0]]
    return waste_type[trash_list[0]] + " and " + format_trash_list(trash_list[1:])

class MessageFormater:
    """Formats the messages to be sent."""

    def __init__(self, food_master):
        self.food_master = food_master

    def get_role_update_text(self, ex_food_master):
        """Returns the text to be sent to the global
        chat when the food master changes."""
        return f"{ex_food_master} is no more the food master. " + \
               f"{self.food_master} is the new food master.\n\n"

    # Todo: Update this function with the right action as:
    # Hi {Food master}! Tomorrow you need to get the Normal trashes out and the Bio trashes out.
    def get_daily_update_text(self, schedule):
        """Returns the text to be send to the food master every day for the tasks of the day."""
        return f"Hi { self.food_master }! You need to get the trashes out tomorrow.\n\n"

    def get_weekly_schedule_text(self, schedule):
        """Returns the text to be send to the food master every week for the tasks of the week.
        Example: schedule = {
            datetime.date(2021, 6, 1): [1, 2], 
            datetime.date(2021, 6, 2): [0, 3]
        } """
        message = f"Hello {self.food_master},\n" + \
            "for this week you need to put these trashes in front the house before 7:00am:\n"
        for date in schedule:
            message = message + \
            f"The {format_trash_list(schedule[date])} on {calendar.day_name[date.weekday()]}.\n"
        message = message + "Thank you !\n"
        return message
