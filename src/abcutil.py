import time


def get_now_str(format='%Y%m%d%H%M%S') -> str:
    return time.strftime(format)


def isTrue(obj):
    pass


def seconds2hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return int(hours), int(minutes), int(seconds)
