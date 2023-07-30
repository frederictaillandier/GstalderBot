""" Test WeRecycleTrashScheduleGrabber """
import datetime
from srcs.trash_schedule_grabbers.we_recycle_trash_schedule_grabber import (
    WeRecycleTrashScheduleGrabber,
)


def test_we_recycle_trash_schedule_grabber_returns_waste_type_1_in_june():
    """Test that WeRecycleTrashScheduleGrabber returns the correct data"""
    grabber = WeRecycleTrashScheduleGrabber()
    schedule = grabber.grab(
        datetime.datetime(2023, 7, 26), datetime.datetime(2023, 7, 26)
    )
    assert schedule[0]["waste_type"] == 0
