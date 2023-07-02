""" Main file of the program."""
import datetime
import json
import os
import argparse

from food_master_finder import FoodMasterFinder
from trash_schedule_grabbers.trash_schedule_grabber import TrashScheduleGrabber
from notification_producer import NotificationProducer

def main():
    """Main function of the program."""
    # get config and builders
    config = json.loads(os.environ["GSTALDERCONFIG"])
    trash_schedule_grabber = TrashScheduleGrabber()

    food_master_finder = FoodMasterFinder(
        config["flatmates"],
        datetime.date.today() + datetime.timedelta(days=1)
        )

    notif_producer = NotificationProducer(
        food_master_finder,
        trash_schedule_grabber,
        config
        )

    parser = argparse.ArgumentParser()
    parser.add_argument("--weekly", help="send weekly schedule", action="store_true")
    args = parser.parse_args()
    if args.weekly:
        notif_producer.send_weekly_schedule()
        notif_producer.send_food_master_change()
    notif_producer.send_daily_schedule()
    return 0

if __name__ == "__main__":
    main()
