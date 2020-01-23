from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from datetime import datetime
from project_e.customers.models import Customer
from project_e.dealers.models import Dealer
from project_e.contractors.models import Contractor



class Job(models.Model):
    #job_id = models.AutoField(primary_key=True)
    cust_id = models.IntegerField(default=0)
    #cust_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    dealer_id = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    #salesman_id = models.IntegerField()
    cont_id = models.ForeignKey(Contractor, blank=True, null=True, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(_("Date of Sale"), default=datetime.now, blank=True)
    contractor_notified_date = models.DateTimeField(_("Date Given To Contractor"), blank=True, null=True)
    contractor_completed_date = models.DateTimeField(_("Date Completed by Contractor"), blank=True, null=True)
    pref_inst_day1 = models.DateTimeField(_("Preferred Installation Time 1"), blank=True, null=True)
    pref_inst_day2 = models.DateTimeField(_("Preferred Installation Time 2"), blank=True, null=True)
    pref_inst_day3 = models.DateTimeField(_("Preferred Installation Time 3"), blank=True, null=True)

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"pk": self.id})
