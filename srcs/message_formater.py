import calendar

waste_type = ["We recycle", "Normal", "Bio", "Carboard", "Paper", "Unknown", "Unknown2", "Hazard"] 

def format_trash_list(trash_list):
    if len(trash_list) == 1:
        return waste_type[trash_list[0]]
    else:
        return waste_type[trash_list[0]] + " and " + format_trash_list(trash_list[1:])

class MessageFormater:

    def __init__(self, food_master):
        self.food_master = food_master

    def get_role_update_text(self, ex_food_master):
        return "{0} is no more the food master. {1} is the new food master.\n\n".format(ex_food_master, self.food_master)

    def get_daily_update_text(self, schedule):
        return "Hi {0}! You need to get the trashes out tomorrow.\n\n".format(self.food_master)

    def get_weekly_schedule_text(self, schedule):
        message = "Hello {0},\nfor this week you need to put these trashes in front the house before 7:00am:\n".format(self.food_master)
        for date in schedule:
            # Todo: handling multiple trash type on a day
            message = message + "The {0} on {1}.\n".format(format_trash_list(schedule[date]), calendar.day_name[date.weekday()])
        message = message + "Thank you !\n"
        return message
