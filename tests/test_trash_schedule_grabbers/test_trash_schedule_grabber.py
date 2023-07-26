""" Test the trash schedule grabber."""

import datetime
from srcs.trash_schedule_grabbers.trash_schedule_grabber \
    import TrashScheduleGrabber

def test_trash_schedule_grabber_returns_1_on_1_06_2023():
    """ Test that TrashScheduleGrabber returns the correct data """
    grabber = TrashScheduleGrabber()
    schedule = grabber.get_schedule(datetime.datetime(2023, 6, 1), datetime.datetime(2023, 6, 2))
    assert schedule[datetime.datetime(2023, 6, 1, 0, 0)][0] == 1

def test_trash_schedule_grabber_return_0_on_26_07_2023():
    """ Test that TrashScheduleGrabber returns the correct data """
    grabber = TrashScheduleGrabber()
    schedule = grabber.get_schedule(datetime.datetime(2023, 7, 26), datetime.datetime(2023, 7, 27))
    assert 0 in schedule[datetime.datetime(2023, 7, 26, 0, 0)]
