import requests
import datetime
from dateutil.parser import parse

def trim_date(date):
    return {
        "date": parse(date["date"]).replace(tzinfo=None),
        "waste_type": date["waste_type"]
    }

def trim_schedule(schedule):
    return list(map(lambda date: trim_date(date), schedule))

class AdliwsilTrashScheduleGrabber:
    def __init__(self):
        self.url = "https://adliswil.entsorglos.swiss/backend/widget/calendar-dates/{0}-{1}/"

    def grab(self, from_date, until_date):
        result = requests.get(self.url.format(from_date.month, from_date.year))
        if result.status_code != 200:
            raise Exception("Could not get trash schedule from " + self.url)
        raw_schedule = list(result.json()['results']['events'])
        filtered_schedule = list(filter(lambda event: event["date"] >= from_date and event["date"] <= until_date, raw_schedule))
        trimmed_schedule = trim_schedule(filtered_schedule)
        return trimmed_schedule

class WeRecycleTrashScheduleGrabber:
    def __init__(self):
        pass

    def grab(self, date, until):
        return []


class TrashScheduleGrabber:
    def __init__(self):
        self.raw_grabbers = [AdliwsilTrashScheduleGrabber(), WeRecycleTrashScheduleGrabber()]
        
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
    
