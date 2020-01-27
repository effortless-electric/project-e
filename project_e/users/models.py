from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.urls import reverse

from project_e.dealers.models import Dealer
from project_e.contractors.models import Contractor

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    # First Name and Last Name do not cover name patterns
    # around the globe.
    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) # can login 
    staff = models.BooleanField(default=False) # staff user non superuser
    admin = models.BooleanField(default=False) # superuser 
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Name of User", blank=True, max_length=255)
    #dealer = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, blank=True, null=True, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealer, blank=True, null=True, on_delete=models.CASCADE)
    sales = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email' 
    # USERNAME_FIELD is required by default but I changed it to email
    REQUIRED_FIELDS = [] #['full_name'] would go here if you want the users full name

    objects = UserManager()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active





class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email