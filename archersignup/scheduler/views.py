from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import forms
from .forms import SignUpForm
from .models import signup
from django.contrib import messages

def home(request):
    return HttpResponse('Home') 

def all_signups(request):
    signup_list = signup.objects.all()
    return render(request, 'scheduler/all_signups.html', {'signup_list': signup_list})
    
def regpage(request):
    if request.POST:
        form = SignUpForm(request.POST)
        signup_list = signup.objects.all()
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
    