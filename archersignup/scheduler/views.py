from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from .models import signup
from django.contrib import messages
import datetime as dt
from .dayFormat import get_day_value
from .dayFormat import dateFinder

def home():
    return HttpResponse('Home') 

def all_signups(request):
    signup_list = signup.objects.all()
    WeeksDates = dateFinder()
    displaydays = {"mon":[], "tue":[], "wed":[], "thu":[], "fri":[], "sat":[], "sun":[]}
    for day in signup_list:
        day_info = []
        day_info.extend([day.Pick_Time, day.Name])
        result = get_day_value(day.Pick_Day)
        if result is not None:
            displaydays[result].append(day_info)
            #print(displaydays)

        #print(result)

    return render(request, 'scheduler/all_signups.html', {'signup_list': signup_list, 'displaydays': displaydays, 'WeeksDates': WeeksDates})
    
def regpage(request):
    if request.POST:
        dayweek = dt.date(int(request.POST.get('Pick_Day')[0:4]), int(request.POST.get('Pick_Day')[5:7]), int(request.POST.get('Pick_Day')[8:10])).weekday()
        form = SignUpForm(request.POST)
        signup_list = signup.objects.all()
        if form.is_valid:
            x = 0
            for object in signup_list:
                today = dt.date.today()
                today_week = today.isocalendar().week
                if object.Pick_Day.isocalendar().week < today_week:
                    object.delete()
                if request.POST['Pick_Day'] == str(object.Pick_Day) and request.POST['Pick_Time'] == str(object.Pick_Time):
                    x += 1
                if x > 2:
                    messages.warning(request, 'The selected time slot is already filled.')
                    break
            if x <= 2:
                if dayweek == 5 or dayweek == 6 or (dayweek == 4 and request.POST.get('Pick_Time') == '9:30-10:00') or (dayweek == 0 and request.POST.get('Pick_Time') == '9:30-10:00'):
                    messages.warning(request, 'Archers period not available Friday-Monday')
                elif dt.datetime.strptime(request.POST['Pick_Day'], "%Y-%m-%d").isocalendar().week < today_week:
                    messages.warning(request, 'Cannot signup for previous weeks')
                else:
                    form.save()
                    return redirect(all_signups)  
        return HttpResponseRedirect("/")
    return render(request, 'scheduler/signup.html', {'form': SignUpForm})
    