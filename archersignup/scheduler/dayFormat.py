import datetime as dt

def dateFinder():
    today = dt.datetime.now()
    today=(str(today.strftime('%Y-%U')))
    r = dt.datetime.strptime(str(today) + '-1', "%Y-%W-%w")
    rdate = dt.date(int(r.strftime('%Y')), int(r.strftime('%m')), int(r.strftime('%d')))
    daysOfWeek = {"mon":'', "tue":'', "wed":'', "thu":'', "fri":''}
    x = 0
    for day in daysOfWeek:
        daysOfWeek[day] = (rdate + dt.timedelta(days=x)).day
        x += 1
    
    return(daysOfWeek)

def get_day_value(day):
    dayValue = {'mon': '0', 'tue': '1', 'wed': '2', 'thu': '3', 'fri': '4', 'sat': '5', 'sun': '6',}
    valueDay = {'0': 'mon', '1': 'tue', '2': 'wed', '3': 'thu', '4': 'fri', '5': 'sat', '6': 'sun',}
    today = dt.date.today()
    today_week = today.isocalendar().week
    event_week = day.isocalendar().week
    if today_week == event_week:
       theday = day.weekday()
       for i in dayValue:
            if dayValue[i] == str(theday):
                event_this_week = valueDay[str(theday)]
                return (str(event_this_week))
