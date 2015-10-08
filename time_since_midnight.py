def time_since_midnight(seconds):
    time = seconds.split(':')
    seconds_hours = int(time[0]) * 3600
    seconds_minutes = int(time[1]) * 60
    seconds_seconds = int(time[2])
    seconds = seconds_hours + seconds_minutes + seconds_seconds
    return seconds
