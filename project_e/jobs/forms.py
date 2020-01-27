from django import forms
from project_e.jobs.models import Job

class ContractForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    # phone = PhoneNumberField(label="Phone Number")
    vin = forms.CharField(label="VIN", min_length=17, max_length=17)
    car_make = forms.CharField(label="Make", max_length=100)
    car_model = forms.CharField(label="Model", max_length=100)
    notes = forms.CharField(label="Notes", max_length=1000)
   