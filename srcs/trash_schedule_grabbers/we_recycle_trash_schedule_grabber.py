"""Module to fetch the trash schedule from the WeRecycle company."""
import datetime


class WeRecycleTrashScheduleGrabber:
    """Class to fetch the trash schedule from the WeRecycle company."""

    RAW_DATES = (
        {"date": datetime.datetime(2023, 7, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 7, 26), "waste_type": 0},
        {"date": datetime.datetime(2023, 8, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 8, 28), "waste_type": 0},
        {"date": datetime.datetime(2023, 9, 11), "waste_type": 0},
        {"date": datetime.datetime(2023, 9, 26), "waste_type": 0},
    )

    def grab(self, date, until):
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
