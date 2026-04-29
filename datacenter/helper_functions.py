from django.utils.timezone import localtime,now
import math


seconds_in_hour = 3600
seconds_in_minute = 60


def get_duration(visit):
    entry_localtime = localtime(visit.entered_at)
    if visit.leaved_at:
        return now() - entry_localtime
    else:
        leaved_localtime = localtime(visit.leaved_at)
        return leaved_localtime - entry_localtime
    
    
def format_duration(duration):
    seconds = math.trunc(duration.total_seconds())
    hours = seconds//seconds_in_hour
    minutes = (seconds % seconds_in_hour)//seconds_in_minute
    second = seconds % seconds_in_minute
    return f"{hours}:{minutes}:{second}"


def is_visit_long(duration,limit):
    total_limit = limit * seconds_in_minute
    long_visit = duration.total_seconds() < total_limit
    return long_visit