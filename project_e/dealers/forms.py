from django import forms

class DealerCreationForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField() #Address
