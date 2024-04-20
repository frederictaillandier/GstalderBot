"""Module to find the food master for a given date."""
import datetime
import requests

WEEKS_PER_YEAR = 52
GET_CHANNELS_URL = "https://api.telegram.org/bot{}/getChat?chat_id={}"

class FoodMasterFinder:
    """Class to find the food master for a given date."""

    def __init__(self, config: dict, tomorrow: datetime.datetime):
        self.flatmates: dict = config["flatmates"]
        for flatmate in self.flatmates:          
            result = requests.get(f"""https://api.telegram.org/bot{config["bot_token"]}/getChat?chat_id={flatmate["chat_id"]}""", timeout=5)
            result.raise_for_status()
            title = result.json()["result"]["title"]
            print(title)
            # Remove the start of the sentence
            flatmate["name"] = title[17:]

        self.tomorrow: datetime.datetime = tomorrow

    def get_current(self) -> dict:
        """Returns the food master for the current week.
        Example: {"name": Jose, "chat_id": 9999999999999 }
        """
        week_number: int = (self.tomorrow.isocalendar()[1]) % WEEKS_PER_YEAR
        food_master: dict = self.flatmates[week_number % len(self.flatmates)]
        return food_master

    def get_previous(self) -> dict[str, str]:
        """Returns the food master for the previous week."""
        week_number: int = (self.tomorrow.isocalendar()[1]) % WEEKS_PER_YEAR
        food_master: dict = self.flatmates[(week_number - 1) % len(self.flatmates)]
        return food_master

    def get_next(self) -> dict:
        """Returns the food master for the next week."""
        week_number: int = (self.tomorrow.isocalendar()[1]) % WEEKS_PER_YEAR
        food_master: dict = self.flatmates[(week_number + 1) % len(self.flatmates)]
        return food_master
