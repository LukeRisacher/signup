from django import forms
from django.forms import ModelForm
from .models import Offer
    

class DateInput(forms.DateInput):
    input_type = 'date'
 
class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
        widgets = {
                'Pick_Day': DateInput(),
            }
        
