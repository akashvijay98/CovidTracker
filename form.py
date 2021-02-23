from django import forms
from .models import covid_data

class covidData(forms.Form):
	class meta:
		model = covid_data
		fields = '__all__'