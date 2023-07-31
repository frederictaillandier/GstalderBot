"""Module to fetch the trash schedule from different providers."""

import datetime
from .adliswil_trash_schedule_grabber import (
    AdliwsilTrashScheduleGrabber,
)
from .we_recycle_trash_schedule_grabber import (
    WeRecycleTrashScheduleGrabber,
)


class TrashScheduleGrabber:
    """Class to fetch the trash schedule from different providers."""

    def __init__(self):
        self.raw_grabbers: tuple(object) = (
            AdliwsilTrashScheduleGrabber(),
            WeRecycleTrashScheduleGrabber(),
        )

    def get_schedule(
        self, from_date: datetime.datetime = None, until_date: datetime.datetime = None
    ) -> dict:
        """get the trash schedule from the different providers and return it as a dict
        Example:
        [
            { "date": datetime.datetime(2021, 6, 1, 0, 0), "waste_type": [1] },
            { "date": datetime.datetime(2021, 6, 2, 0, 0), "waste_type": [0,5] },
            { "date": datetime.datetime(2021, 6, 3, 0, 0), "waste_type": [6] }
        ]
        """
        raw_schedule: list[dict] = []

        # making sure the dates are set and using tomorrow if not
        if from_date is None:
            from_date = datetime.datetime.today()
        if until_date is None:
            until_date = from_date + datetime.timedelta(days=1)

        # grab events for all the event grabbers
        for grabber in self.raw_grabbers:
            raw_schedule = raw_schedule + grabber.grab(from_date, until_date)

        schedule: dict[datetime.datetime, list[int]] = {}
        for event in raw_schedule:
            if event["date"] not in schedule:
                schedule[event["date"]] = []
            schedule[event["date"]].append(event["waste_type"])
        return schedule
