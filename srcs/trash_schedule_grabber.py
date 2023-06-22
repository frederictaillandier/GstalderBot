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

class TrashScheduleGrabber:
    def __init__(self, url):
        self.url = url

    def get_schedule(self, date = None, until_date = None):
        if date is None:
            date = datetime.datetime.today() + datetime.timedelta(days=1)
        if until_date is None:
            until_date = date
        result = requests.get(self.url)
        if result.status_code != 200:
            raise Exception("Could not get trash schedule from " + self.url)
        trimmed_schedule = trim_schedule(result.json()['results']['events'])
        return list(filter(lambda event: event["date"] >= date and event["date"] <= until_date, trimmed_schedule))

if __name__ == "__main__":
    grabber = TrashScheduleGrabber("https://adliswil.entsorglos.swiss/backend/widget/calendar-dates/7-2023/")
    print(grabber.get_schedule( datetime.datetime.today() + datetime.timedelta(days=1), datetime.datetime.today() + datetime.timedelta(days=8)))
