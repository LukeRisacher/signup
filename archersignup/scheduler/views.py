from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import forms
from .forms import SignUpForm
from .models import signup
from django.contrib import messages
import datetime as dt
import json
from .dayFormat import get_day_value
from pprint import pprint

def home(request):
    return HttpResponse('Home') 

def all_signups(request):
    signup_list = signup.objects.all()
    displaydays = {"mon":[], "tue":[], "wed":[], "thu":[], "fri":[], "sat":[], "sun":[]}
    for day in signup_list:
        day_info = []
        day_info.extend([day.Pick_Time, day.Name])
        result = get_day_value(day.Pick_Day)
        if result is not None:
            displaydays[result].append(day_info)
            print(displaydays)
            #print(displaydays['wed'])

        #print(result)

    return render(request, 'scheduler/all_signups.html', {'signup_list': signup_list, 'displaydays': displaydays})
    
def regpage(request):
    if request.POST:
        form = SignUpForm(request.POST)
        signup_list = signup.objects.all()
        day = dt.date(int(request.POST['Pick_Day'][0:4]), int(request.POST['Pick_Day'][5:7]), int(request.POST['Pick_Day'][8:]))
        if form.is_valid:
            x = 0
            for object in signup_list:
                if request.POST['Pick_Day'] == str(object.Pick_Day) and request.POST['Pick_Time'] == str(object.Pick_Time):
                    x = 1
                    messages.warning(request, 'The selected time slot is already filled.')
            if x == 0:
                form.save()

                return redirect(all_signups)   
        return HttpResponseRedirect("/")
    return render(request, 'scheduler/signup.html', {'form': SignUpForm})
    