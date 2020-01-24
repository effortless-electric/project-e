from django import forms
from .models import Contractor

class ContractorCreationForm(forms.ModelForm):
    cont_name = forms.CharField()
    cont_email = forms.CharField()
    address = forms.CharField()
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.CharField()
    notes = forms.CharField()
    class Meta:
        model = Contractor
        fields = ('cont_name', 'cont_email', 'fname', 'lname', 'phone', 'address')
        