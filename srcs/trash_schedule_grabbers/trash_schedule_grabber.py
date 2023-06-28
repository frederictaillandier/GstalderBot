from .adliswil_trash_schedule_grabber import AdliwsilTrashScheduleGrabber
from .we_recycle_trash_schedule_grabber import WeRecycleTrashScheduleGrabber
import datetime

class TrashScheduleGrabber:
    def __init__(self):
        self.raw_grabbers = [AdliwsilTrashScheduleGrabber(), 
                             WeRecycleTrashScheduleGrabber()]
        
    def get_schedule(self, from_date = None, until_date = None):
        raw_schedule = []
       
        # making sure the dates are set and using tomorrow if not
        if from_date is None:
            from_date = datetime.datetime.today() + datetime.timedelta(days=1)
        if until_date is None:
            until_date = from_date

        # grab events for all the event grabbers
        for grabber in self.raw_grabbers:
            raw_schedule = raw_schedule + grabber.grab(from_date, until_date)        

        schedule = {}
        for event in raw_schedule:
            if event["date"] not in schedule:
                schedule[event["date"]] = []
            schedule[event["date"]].append(event["waste_type"])

        return schedule
