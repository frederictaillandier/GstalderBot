import calendar

class MessageFormater:
    waste_type = ["We recycle", "Normal", "Bio", "Carboard", "Paper", "Unknown", "Unknown2", "Hazard"] 

    def __init__(self, food_master):
        self.food_master = food_master

    def get_role_update_text(self, ex_food_master):
        return "{0} is no more the food master. {1} is the new food master.\n\n".format(ex_food_master, self.food_master)

    def get_daily_update_text(self, schedule):
        return "Hi {0}! You need to get the trashes out tomorrow.\n\n".format(self.food_master)

    def get_weekly_schedule_text(self, schedule):
        message = "Hello {0},\nfor this week you need to put these trashes in front the house before 7:00am:\n".format(self.food_master)
        for date in schedule:
            message = message + "The {0} on {1}.\n".format(self.waste_type[schedule[date][0]], calendar.day_name[date.weekday()])
        message = message + "Thank you !\n"
        return message 
