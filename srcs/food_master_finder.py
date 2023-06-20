import datetime

class FoodMasterFinder:
    weeks_calendar_delta = 4

    def __init__(self, flatmates, tomorrow):
        self.flatmates = flatmates
        self.tomorrow = tomorrow

    def get_current(self):
        week_number = (self.tomorrow.isocalendar()[1] + self.weeks_calendar_delta) % 52
        food_master = self.flatmates[week_number % len(self.flatmates)]['name']
        return food_master
    
    def get_previous(self):
        week_number = (self.tomorrow.isocalendar()[1] + self.weeks_calendar_delta) % 52
        food_master = self.flatmates[(week_number - 1) % len(self.flatmates)]['name']
        return food_master
    
    def get_next(self):
        week_number = (self.tomorrow.isocalendar()[1] + self.weeks_calendar_delta) % 52
        food_master = self.flatmates[(week_number + 1) % len(self.flatmates)]['name']
        return food_master

    def get_introduction_text(self):
        return "{0} is no more the food master. {1} is the new food master.\n\n".format(self.get_previous(), self.get_current())
