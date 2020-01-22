from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class Contractor(models.Model):
    #cont_id = HashidAutoField(primary_key=True, allow_int_lookup=True)
    name = models.CharField(_("Contractor Name"), blank=False, max_length=500)
    email = models.EmailField(_("Contractor Email"), blank=False, null=True)
    address = models.CharField(_("Address"), blank=False, max_length=500)
    fname = models.CharField(_("First Name"), blank=False, max_length=30)
    lname = models.CharField(_("Last Name"), blank=False, max_length=30)
    phone = models.CharField(_("Phone Number"), blank=False, max_length=10)
    notes = models.CharField(_("Misc Notes"), blank=False, max_length=500)
    num_installs = models.IntegerField(default=0, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("customers:detail", kwargs={"pk": self.id})
