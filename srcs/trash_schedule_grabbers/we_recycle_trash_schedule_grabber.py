"""Module to fetch the trash schedule from the WeRecycle company."""
class WeRecycleTrashScheduleGrabber:
    """Class to fetch the trash schedule from the WeRecycle company."""
    def __init__(self):
        pass

    def grab(self, date, until):
        """
        Returns a list of dicts of the trash schedule from the Adliswil website.
        Example: 
        [
            { "date": datetime.datetime(2021, 6, 1, 0, 0), "waste_type": [0] },
            { "date": datetime.datetime(2021, 6, 2, 0, 0), "waste_type": [0] },
            { "date": datetime.datetime(2021, 6, 3, 0, 0), "waste_type": [0] },
        ]
        """
        # Todo: implement
        return []
