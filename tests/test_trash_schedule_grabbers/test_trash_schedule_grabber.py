""" Test the trash schedule grabber."""

import datetime
from srcs.trash_schedule_grabbers.trash_schedule_grabber import TrashScheduleGrabber


def test_trash_schedule_grabber_returns_1_on_1_06_2023() -> None:
    """Test that TrashScheduleGrabber returns the correct data"""
    grabber = TrashScheduleGrabber()
    schedule = grabber.get_schedule(
        from_date=datetime.datetime(year=2023, month=6, day=1),
        until_date=datetime.datetime(year=2023, month=6, day=2),
    )
    assert (
        schedule[datetime.datetime(year=2023, month=6, day=1, hour=0, minute=0)][0] == 1
    )


def test_trash_schedule_grabber_return_0_on_26_07_2023() -> None:
    """Test that TrashScheduleGrabber returns the correct data"""
    grabber = TrashScheduleGrabber()
    schedule = grabber.get_schedule(
        from_date=datetime.datetime(2023, 7, 26),
        until_date=datetime.datetime(2023, 7, 27),
    )
    assert (
        0 in schedule[datetime.datetime(year=2023, month=7, day=26, hour=0, minute=0)]
    )
