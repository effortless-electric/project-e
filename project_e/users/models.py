from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from project_e.dealers.models import Dealer
from project_e.contractors.models import Contractor

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    #dealer = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, blank=True, null=True, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    sales = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
