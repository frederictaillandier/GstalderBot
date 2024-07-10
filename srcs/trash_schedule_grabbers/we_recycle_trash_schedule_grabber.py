"""Module to fetch the trash schedule from the WeRecycle company."""
import datetime
from typing import Any


class WeRecycleTrashScheduleGrabber:
    """Class to fetch the trash schedule from the WeRecycle company."""

    RAW_DATES: tuple = (
        {"date": datetime.datetime(2024, 4, 9), "waste_type": 0},
        {"date": datetime.datetime(2024, 4, 25), "waste_type": 0},
        {"date": datetime.datetime(2024, 5, 13), "waste_type": 0},
        {"date": datetime.datetime(2024, 5, 28), "waste_type": 0},
        {"date": datetime.datetime(2024, 6, 11), "waste_type": 0},
        {"date": datetime.datetime(2024, 6, 25), "waste_type": 0},
        {"date": datetime.datetime(2024, 7, 26), "waste_type": 0},
        {"date": datetime.datetime(2024, 8, 12), "waste_type": 0},
        {"date": datetime.datetime(2024, 8, 27), "waste_type": 0},
        {"date": datetime.datetime(2024, 9, 9), "waste_type": 0},
        {"date": datetime.datetime(2024, 9, 25), "waste_type": 0},
    )

    def grab(self, date: datetime.datetime, until: datetime.datetime) -> list:
        """
        Returns a list of dicts of the trash schedule from the Adliswil website.
        Example:
        {
            { "date": datetime.datetime(2021, 6, 1, 0, 0), "waste_type": [0] },
            { "date": datetime.datetime(2021, 6, 2, 0, 0), "waste_type": [0] },
            { "date": datetime.datetime(2021, 6, 3, 0, 0), "waste_type": [0] },
        }
        """
        return list(
            filter(
                lambda event: event["date"] >= date and event["date"] <= until,
                self.RAW_DATES,
            )
        )
