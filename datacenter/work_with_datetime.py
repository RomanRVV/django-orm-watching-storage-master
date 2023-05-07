from django.utils import timezone


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
