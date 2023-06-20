import datetime

class FoodMasterFinder:
    weeks_calendar_delta = 4

    def __init__(self, flatmates, tomorrow):
        self.flatmates = flatmates
        self.tomorrow = tomorrow

    def getCurrent(self):
        week_number = (self.tomorrow.isocalendar()[1] + self.weeks_calendar_delta) % 52
        FoodMaster = self.flatmates[week_number % len(self.flatmates)]['name']
        return FoodMaster
    
    def getPrevious(self):
        week_number = (self.tomorrow.isocalendar()[1] + self.weeks_calendar_delta) % 52
        FoodMaster = self.flatmates[(week_number - 1) % len(self.flatmates)]['name']
        return FoodMaster
    
    def getNext(self):
        week_number = (self.tomorrow.isocalendar()[1] + self.weeks_calendar_delta) % 52
        FoodMaster = self.flatmates[(week_number + 1) % len(self.flatmates)]['name']
        return FoodMaster

    def getIntroductionText(self):
        return "{0} is no more the food master. {1} is the new food master.\n\n".format(self.getPrevious(), self.getCurrent())
