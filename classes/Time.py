import datetime
class Time:
    def __str__(self):
        now=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
        return now.strftime("%m/%d/%Y %H:%M:%S")


