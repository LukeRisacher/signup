import datetime as dt

day = dt.date(2022, 9, 21)

def get_day_value(day):
    
    dayValue = {'mon': '0', 'tue': '1', 'wed': '2', 'thu': '3', 'fri': '4', 'sat': '5', 'sun': '6',}
    valueDay = {'0': 'mon', '1': '0', '2': 'wed', '3': 'thu', '4': 'fri', '5': 'sat', '6': 'sun',}
    today = dt.date.today()
    today_week = today.isocalendar()
    today_week = today_week.week
    event_week = day.isocalendar()
    event_week = event_week.week
    if today_week == event_week:
       theday = day.weekday()
       for i in dayValue:
            if dayValue[i] == str(theday):
                event_this_week = valueDay[str(theday)]
                return (str(event_this_week))
get_day_value(day)