def format_time(hours, minutes, seconds):
    def format(x):
        return str(x).rjust(2, '0')
    
    hours = format(hours) + ':'
    minutes = format(minutes) + ':'
    seconds = format(seconds)

    return hours + minutes + seconds