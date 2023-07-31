"""Module to fetch the trash schedule from the Adliswil website."""
import requests
import datetime
from dateutil.parser import parse


def trim_date(date: dict) -> dict:
    """Returns a dict with only the date and the waste type.
    Example:
    { "date": "2021-06-01T00:00:00+02:00", "name": "trashes", "waste_type": 1 }\n
    ->\n
    { "date": datetime.datetime(2021, 6, 1, 0, 0), "waste_type": 1 }
    """
    return {
        "date": parse(date["date"]).replace(tzinfo=None, hour=0, minute=0, second=0),
        "waste_type": date["waste_type"],
    }


def trim_schedule(schedule: list) -> list:
    """Returns a list of dicts with only the date and the waste type."""
    return list(map(trim_date, schedule))


class AdliwsilTrashScheduleGrabber:
    """Class to fetch the trash schedule from the Adliswil website."""

    def __init__(self):
        self.url = (
            "https://adliswil.entsorglos.swiss/backend/widget/calendar-dates/{0}-{1}/"
        )

    def grab(self, from_date: datetime, until_date: datetime) -> list:
        """
        Returns a list of dicts of the trash schedule from the Adliswil website.
        Example:
        [
            { "date": datetime.datetime(2021, 6, 1, 0, 0), "waste_type": [1] },
            { "date": datetime.datetime(2021, 6, 2, 0, 0), "waste_type": [2,5] },
            { "date": datetime.datetime(2021, 6, 3, 0, 0), "waste_type": [6] },
        ]
        """
        result = requests.get(
            self.url.format(from_date.month, from_date.year), timeout=5
        )
        if result.status_code != 200:
            raise RuntimeError(f"Could not get trash schedule from {self.url}")
        raw_schedule = list(result.json()["results"]["events"])
        trimmed_schedule = trim_schedule(raw_schedule)
        filtered_schedule = list(
            filter(
                lambda event: event["date"] >= from_date
                and event["date"] <= until_date,
                trimmed_schedule,
            )
        )
        return filtered_schedule
