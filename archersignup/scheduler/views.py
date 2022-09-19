from django.shortcuts import render
from .forms import OfferForm

# Create your views here.
def signUp(request):
    form = OfferForm()
    return render(request, 'scheduler/test.html', {'form':form})
    # if response.method == 'POST':
    #     form = DateInput(response.post)
    #     if form.is_valid():
    #         form.save()
    #     return render(response, 'standing/scheduler.html')
