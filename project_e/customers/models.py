from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
#from hashid_field import HashidAutoField
#from hashid_field.rest import HashidSerializerCharField
#from rest_framework import serializers
#from project_e.dealers.models import Dealer
#from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUsera

# Create your models here.
class Customer(models.Model):
    #cust_id = models.AutoField(primary_key=True)
    email = models.EmailField(_("Customer Email"), blank=False, null=True)
    address = models.CharField(_("Address"), blank=False, max_length=500)
    fname = models.CharField(_("First Name"), blank=False, max_length=30)
    lname = models.CharField(_("Last Name"), blank=False, max_length=30)
    phone = models.CharField(_("Phone Number"), blank=False, max_length=10)
    notes = models.CharField(_("Misc Notes"), blank=False, max_length=500)
    vin = models.CharField(_("VIN"), blank=False, max_length=50)
    car_make = models.CharField(_("Car Make"), blank=True, max_length=30)
    car_model = models.CharField(_("Car Model"), blank=True, max_length=30)
    #salesman and dealer_id can be joined in the jobs table

    def get_absolute_url(self):
        return reverse("customers:detail", kwargs={"pk": self.id})
