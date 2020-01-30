from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model

from project_e.customers.models import Customer
from project_e.dealers.models import Dealer
from project_e.contractors.models import Contractor

User = get_user_model()


class Job(models.Model):
    customer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='buyer_to_job')
    dealership = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='seller_to_job')
    cont_id = models.ForeignKey(Contractor, blank=True, null=True, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(_("Date of Sale"), default=datetime.now, blank=True)
    contractor_notified_date = models.DateTimeField(_("Date Given To Contractor"), blank=True, null=True)
    contractor_completed_date = models.DateTimeField(_("Date Completed by Contractor"), blank=True, null=True)
    pref_inst_day1 = models.DateTimeField(_("Preferred Installation Time 1"), blank=True, null=True)
    pref_inst_day2 = models.DateTimeField(_("Preferred Installation Time 2"), blank=True, null=True)
    pref_inst_day3 = models.DateTimeField(_("Preferred Installation Time 3"), blank=True, null=True)
    selected_install_day = models.DateTimeField(_("Selected Time"), blank=True, null=True)
    vin = models.CharField(max_length=17, blank=True, null=True)
    car_make = models.CharField(max_length=100, blank=True, null=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"pk": self.id})

    def get_status(self): 
        return self.selected_install_day is not None if 'pending' else 'installing'

    def get_install(self): 
        return self.selected_install_day is None if self.pref_inst_day1 else self.selected_install_day