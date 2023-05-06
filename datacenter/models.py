from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


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


def get_duration(visit):
    entered_at = timezone.localtime(visit.entered_at)
    leaved_at = timezone.localtime(visit.leaved_at)
    time_now = timezone.localtime()
    if leaved_at:
        delta = leaved_at - entered_at
    else:
        delta = time_now - entered_at
    return delta


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return f'{str(hours).split(".")[0]}ч {str(minutes).split(".")[0]}мин'


def is_visit_long(visit, minutes=60):
    visit_minutes = get_duration(visit).total_seconds() // 60
    if visit_minutes > minutes:
        return True
    else:
        return False
