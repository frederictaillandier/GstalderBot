import datetime
import json
import os
from srcs.notification_producer import NotificationProducer


class FoodMasterFinderMock:
    """MOCK FoodMasterFinder class"""

    def __init__(self, config):
        self.current = config["flatmates"][0]
        self.next = config["flatmates"][1]

    def get_current(self):
        """MOCK Returns the food master for the current week."""
        return self.current

    def get_previous(self):
        """MOCK Returns the food master for the previous week."""
        return self.next


class TrashScheduleGrabberMock:
    """MOCK TrashScheduleGrabber class"""

    def get_schedule(
        self, from_date=None, until_date=None
    ):  # pylint: disable=unused-argument
        """MOCK Returns the trash schedule for the given period."""
        return {
            datetime.datetime(year=2021, month=1, day=1): [1, 2, 3]
        }  # TODO: change to enum


class TrashScheduleGrabberMockNoData:
    """MOCK TrashScheduleGrabber class with no data"""

    def get_schedule(
        self, from_date=None, until_date=None
    ):  # pylint: disable=unused-argument
        """MOCK Returns the trash schedule for the given period."""
        return {}


def test_notification_producer_send_weelkly():
    """Test the NotificationProducer class"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    producer = NotificationProducer(
        FoodMasterFinderMock(config), TrashScheduleGrabberMock(), config=config
    )
    mock_food_master_name = config["flatmates"][0]["name"]

    response = producer.send_weekly_schedule()
    assert (
        response["result"]["text"]
        == f"Hello {mock_food_master_name},\n"
        + "for this week you need to put these trashes in front the house before 7:00am:\n"
        + "The Normal and Bio and Carboard on Friday.\n"
        + "Thank you !"
    )


def test_notification_producer_send_daily():
    """Test the NotificationProducer class"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    producer = NotificationProducer(
        FoodMasterFinderMock(config), TrashScheduleGrabberMock(), config=config
    )
    response = producer.send_daily_schedule()
    assert (
        response["result"]["text"]
        == f"Hi {config['flatmates'][0]['name']}! "
        + "Don't forget to take out the Normal and Bio "
        + "and Carboard before 7am tomorrow.\nHave a nice evening."
    )


def test_notification_producer_send_food_master_change():
    """Test the NotificationProducer class"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    producer = NotificationProducer(
        FoodMasterFinderMock(config), TrashScheduleGrabberMock(), config=config
    )
    response = producer.send_food_master_change()
    assert config["flatmates"][1]["name"] in response["result"]["text"]
    assert config["flatmates"][0]["name"] in response["result"]["text"]


def test_notification_producer_send_food_master_change_no_data():
    """Test the NotificationProducer daily notification with no data included"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    producer = NotificationProducer(
        FoodMasterFinderMock(config), TrashScheduleGrabberMockNoData(), config=config
    )
    response = producer.send_daily_schedule()
    assert (
        response["result"]["text"]
        == f"Hi {config['flatmates'][0]['name']}! "
        + "No trash pickup for tomorrow, have a nice evening!"
    )
