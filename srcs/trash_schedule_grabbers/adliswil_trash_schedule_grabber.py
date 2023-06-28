import requests
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
        trimmed_schedule = trim_schedule(raw_schedule)
        filtered_schedule = list(filter(lambda event: event["date"] >= from_date and event["date"] <= until_date, trimmed_schedule))

        return filtered_schedule