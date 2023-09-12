"""Module to fetch the trash schedule from the WeRecycle company."""
import datetime
from typing import Any


class WeRecycleTrashScheduleGrabber:
    """Class to fetch the trash schedule from the WeRecycle company."""

    RAW_DATES: tuple = (
        {"date": datetime.datetime(2023, 7, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 7, 26), "waste_type": 0},
        {"date": datetime.datetime(2023, 8, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 8, 28), "waste_type": 0},
        {"date": datetime.datetime(2023, 9, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 9, 26), "waste_type": 0},
        {"date": datetime.datetime(2023, 10, 10), "waste_type": 0},
        {"date": datetime.datetime(2023, 10, 26), "waste_type": 0},
        {"date": datetime.datetime(2023, 11, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 11, 27), "waste_type": 0},
        {"date": datetime.datetime(2023, 12, 8), "waste_type": 0},
        {"date": datetime.datetime(2023, 12, 19), "waste_type": 0},
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
