TimetableDict = {}

def update_timetable(func):
    global TimetableDict
    TimetableDict = func
    return TimetableDict