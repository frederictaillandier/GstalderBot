import pytest, datetime
from srcs.trash_schedule_grabber import *

def test_trim_date():
    data = {
        "date": "2021-01-01",
        "name": "Gilles",
        "waste_type": 0
    }
    trimmed_data = trim_date(data)
    assert trimmed_data["date"] == datetime.datetime(2021, 1, 1) and trimmed_data["waste_type"] == 0

def test_trim_date2():
    data = {
        "date": "2021-01-01",
        "name": "Gilles",
        "waste_type": 1
    }
    trimmed_data = trim_date(data)
    with pytest.raises(Exception):
        trimmed_data["name"]


def test_trim_schedule():
    data = [
        {
        "date": "2021-01-01",
        "name": "Gilles",
        "waste_type": 1
        },
        {
        "date": "2021-01-02",
        "name": "Tony",
        "waste_type": 0
        }
    ]
    trimmed_data = trim_schedule(data)
    assert trimmed_data[0]["date"] == datetime.datetime(2021, 1, 1) and trimmed_data[0]["waste_type"] == 1

def test_adliswil_trash_schedule_grabber():
    grabber = AdliwsilTrashScheduleGrabber()
    schedule = grabber.grab(datetime.datetime(2023, 6, 1), datetime.datetime(2023, 6, 1))
    assert schedule[0]["waste_type"] == 2

def test_trash_schedule_grabber():
    grabber = TrashScheduleGrabber()
    schedule = grabber.get_schedule(datetime.datetime(2023, 6, 1), datetime.datetime(2023, 6, 2))
    assert schedule[datetime.datetime(2023, 6, 1, 2, 0)][0] == 1
