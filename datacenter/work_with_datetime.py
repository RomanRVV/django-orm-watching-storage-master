from django.utils import timezone
from datacenter.models import Passcard, Visit, format_duration, get_duration

def get_duration(visit):
    entered_at = timezone.localtime(visit.entered_at)
    time_now = timezone.localtime()
    delta = time_now - entered_at

    return delta


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return f'{hours}ч {minutes}мин'


for visit in Visit.objects.filter(leaved_at__isnull=True):
    print(format_duration(get_duration(visit)))
