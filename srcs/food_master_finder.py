"""Module to find the food master for a given date."""

WEEKS_PER_YEAR = 52


class FoodMasterFinder:
    """Class to find the food master for a given date."""

    def __init__(self, flatmates, tomorrow):
        self.flatmates = flatmates
        self.tomorrow = tomorrow

    def get_current(self):
        """Returns the food master for the current week.
        Example: {"name": Jose, "chat_id": 9999999999999 }
        """
        week_number = (self.tomorrow.isocalendar()[1]) % WEEKS_PER_YEAR
        food_master = self.flatmates[week_number % len(self.flatmates)]
        return food_master

    def get_previous(self):
        """Returns the food master for the previous week."""
        week_number = (self.tomorrow.isocalendar()[1]) % WEEKS_PER_YEAR
        food_master = self.flatmates[(week_number - 1) % len(self.flatmates)]
        return food_master

    def get_next(self):
        """Returns the food master for the next week."""
        week_number = (self.tomorrow.isocalendar()[1]) % WEEKS_PER_YEAR
        food_master = self.flatmates[(week_number + 1) % len(self.flatmates)]
        return food_master
