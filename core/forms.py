from django import forms
from django.forms import ModelForm
from .models import *
import datetime

class DateInput(forms.DateInput):
	input_type = 'date'

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class DriverForm(ModelForm):
	class Meta:
		model = Driver
		fields = '__all__'
		widgets = {'Hire_Date': DateInput(), 'Term_Date': DateInput(), 'DOB': DateInput()}

class EquipmentForm(ModelForm):
	Year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
	class Meta:
		model = Equipment
		fields = '__all__'
		widgets = {'Date_placed': DateInput()}