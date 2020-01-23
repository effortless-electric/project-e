from django import forms as default_form
from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from project_e.dealers.models import Dealer
from project_e.contractors.models import Contractor
#from project_e.customers.models import Customer
#from project_e.customers.forms import DealerAddCustForm

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class UserAddDealerForm(default_form.Form):
    dealercode = default_form.CharField()

    def clean_dealercode(self):
        dealercode = self.cleaned_data["dealercode"]
        if not Dealer.objects.get(id=dealercode):
            raise forms.ValidationError("You have forgotten about Fred!")
        return dealercode

class UserAddContractorForm(default_form.Form):
    contractorcode = default_form.CharField()

    def clean_contractorcode(self):
        contractorcode = self.cleaned_data["contractorcode"]
        if not Contractor.objects.get(id=contractorcode):
            raise forms.ValidationError("You have forgotten about Fred!")
        return contractorcode
