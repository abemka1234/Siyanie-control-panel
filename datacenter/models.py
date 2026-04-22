from django.db import models
from django.utils.timezone import localtime,now
import math


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


def get_duration(visit):
    entry_localtime = localtime(visit.entered_at)
    if visit.leaved_at == None:
        return now() - entry_localtime
    else:
        leaved_localtime = localtime(visit.leaved_at)
        return leaved_localtime - entry_localtime
    
    
def format_duration(duration):
    seconds = math.trunc(duration.total_seconds())
    hours = seconds//3600
    minutes = (seconds % 3600)//60
    second = seconds % 60
    return f"{hours}:{minutes}:{second}"


def is_visit_long(duration,limit):
    total_limit = limit * 60
    long_visit = duration.total_seconds() < total_limit
    return long_visit


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
