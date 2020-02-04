from django import forms

class DealerCreationForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField() #Address

class EmployeeCreationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)

class StaffDealerCreationForm(forms.Form): 
    email = forms.EmailField(label="Email", max_length=100)
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    dealer_name = forms.CharField(label="Dealership Name", max_length=200)
    dealer_address = forms.CharField(label="Dealership Address", max_length=500)