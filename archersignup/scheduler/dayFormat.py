from cgi import test
import datetime as dt


today = dt.date(2022, 9, 18)
def dateFinder():
    today = dt.datetime.now()
    today=(str(today.strftime('%Y-%U')))
    r = dt.datetime.strptime(str(today) + '-1', "%Y-%W-%w")
    rdate = dt.date(int(r.strftime('%Y')), int(r.strftime('%m')), int(r.strftime('%d')))
    daysOfWeek = {"mon":'', "tue":'', "wed":'', "thu":'', "fri":''}
    daysOfWeek['mon'] = (rdate + dt.timedelta(days=0)).day
    daysOfWeek['tue'] = (rdate + dt.timedelta(days=1)).day
    daysOfWeek['wed'] = (rdate + dt.timedelta(days=2)).day
    daysOfWeek['thu'] = (rdate + dt.timedelta(days=3)).day
    daysOfWeek['fri'] = (rdate + dt.timedelta(days=4)).day
    return(daysOfWeek)
day = dt.date(2022, 9, 21)

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
get_day_value(day)