import datetime

from django.views.generic import DetailView, FormView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate

from project_e.customers.models import Customer
from project_e.jobs.forms import ContractForm
from project_e.jobs.models import Job

User = get_user_model()

class JobDetailView(LoginRequiredMixin, DetailView): 
    model = Job

job_detail_view = JobDetailView.as_view()

class JobCreationView(LoginRequiredMixin, FormView):
    model = Job
    template_name = "users/createcust_form.html"
    form_class = ContractForm

    def get_success_url(self):
        return reverse("dealers:job")

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        #print(User.objects.get(self.request.dealership_id))
        full_name = form.cleaned_data["first_name"] + ' ' + form.cleaned_data["last_name"]
        user_email = form.cleaned_data["email"]
        existing_user = User.objects.filter(email=user_email)
        if existing_user: 
            user = existing_user
        else: 
            user = User.objects.create_user(user_email, full_name, "newpass123") # replace password with one time pass

        Job.objects.create(
            customer=user,
            seller=self.request.user,
            dealership=self.request.user.dealership,
            sale_date=datetime.datetime.now().date(),
            vin=form.cleaned_data['vin'],
            car_make=form.cleaned_data['car_make'],
            car_model=form.cleaned_data['car_model'],
            notes=form.cleaned_data['notes'],
        )

        messages.add_message(
            self.request, messages.INFO, "Customer Info successfully updated and job started"
        )
        return super().form_valid(form)

job_creation_view = JobCreationView.as_view()
