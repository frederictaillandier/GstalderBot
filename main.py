""" Main file of the program."""
import datetime
import json
import os

from srcs.food_master_finder import FoodMasterFinder
from srcs.trash_schedule_grabbers.trash_schedule_grabber import TrashScheduleGrabber
from srcs.notification_producer import NotificationProducer


SUNDAY = 6


def main():
    """Main function of the program."""
    # get config and builders
    config = json.loads(os.environ["GSTALDERCONFIG"])
    trash_schedule_grabber = TrashScheduleGrabber()

    food_master_finder = FoodMasterFinder(
        config, datetime.date.today() + datetime.timedelta(days=1)
    )

    notif_producer = NotificationProducer(
        food_master_finder, trash_schedule_grabber, config
    )

    # We send weekly notifications on sundays
    if datetime.datetime.today().weekday() == SUNDAY:
        notif_producer.send_weekly_schedule()
        notif_producer.send_food_master_change()
    notif_producer.send_daily_schedule()
    return 0


if __name__ == "__main__":
    main()
