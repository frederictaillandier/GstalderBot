""" Test AdliswilTrashScheduleGrabber """
import datetime
from srcs.trash_schedule_grabbers.adliswil_trash_schedule_grabber \
    import trim_date, trim_schedule, AdliwsilTrashScheduleGrabber


def test_trim_date_doesnt_corrupt_data():
    """ Test that trim_date doesn't corrupt the data """
    mock = {
        "date": "2021-01-01",
        "name": "Gilles",
        "waste_type": 0
    }
    trimmed_data = trim_date(mock)
    assert trimmed_data["date"] == datetime.datetime(
        2021, 1, 1) and trimmed_data["waste_type"] == 0
    assert len(trimmed_data) == 2
    assert "name" not in trimmed_data


def test_trim_schedule_removes_unnecessary_data():
    """ Test that trim_schedule removes unrequired data """
    mock = [
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
    trimmed_data = trim_schedule(mock)
    assert trimmed_data[0]["date"] == datetime.datetime(2021, 1, 1)
    assert trimmed_data[0]["waste_type"] == 1
    assert len(trimmed_data[0]) == 2


def test_adliswil_trash_schedule_grabber_returns_waste_type_1_in_june():
    """ Test that AdliswilTrashScheduleGrabber returns the correct data"""
    grabber = AdliwsilTrashScheduleGrabber()
    schedule = grabber.grab(datetime.datetime(
        2023, 6, 1), datetime.datetime(2023, 6, 2))
    assert schedule[0]["waste_type"] == 1
