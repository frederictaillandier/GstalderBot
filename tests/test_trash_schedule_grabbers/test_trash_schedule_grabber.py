import datetime
from srcs.trash_schedule_grabbers.trash_schedule_grabber import *

def test_trash_schedule_grabber():
    grabber = TrashScheduleGrabber()
    schedule = grabber.get_schedule(datetime.datetime(2023, 6, 1), datetime.datetime(2023, 6, 2))
    assert schedule[datetime.datetime(2023, 6, 1, 2, 0)][0] == 1
