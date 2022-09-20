from django import forms
from django.forms import ModelForm
from .models import signup
    

class DateInput(forms.DateInput):
    input_type = 'date'



class SignUpForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        widgets = {
                'Pick_Day': DateInput(),
            }
        
