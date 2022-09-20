from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import OfferForm
from .models import Offer

def home(request):
    return HttpResponse('Home') 

def all_signups(request):
    signup_list = Offer.objects.all()
    return render(request, 'scheduler/all_signups.html', {'signup_list': signup_list})
    
def signUp(request):
    if request.POST:
        form = OfferForm(request.POST)
        #print(request.POST)
        if form.is_valid:
            for object in Offer.objects.all():
                print(object)
            form.save()
        return redirect(all_signups)
    return render(request, 'scheduler/test.html', {'form': OfferForm})
    