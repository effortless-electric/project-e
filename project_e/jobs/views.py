import datetime

from django.views.generic import UpdateView, FormView, DetailView, RedirectView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate

from easy_pdf.views import PDFTemplateResponseMixin

from project_e.customers.models import Customer
from project_e.jobs.forms import ContractForm
from project_e.jobs.models import Job


User = get_user_model()

class JobDetailView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['vin', 'contract_price', 'car_year', 'car_make', 'car_model', 'notes']

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, "Job successfully updated"
        )
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs): 
        context = super().get_context_data()
        job = context["job"]
        context["header_table"] = [
            {
                "title": "Sold by: ",
                "body": job.seller.get_full_name
            },
            {
                "title": "Sale date:",
                "body": str(job.sale_date.month) + '/' + str(job.sale_date.day) + '/' + str(job.sale_date.year)
            },
             {
                "title": "Customer:",
                "body": job.customer.full_name
            },
            {
                "title": "Address:",
                "body": job.customer_address
            },
            {
                "title": "Dealership",
                "body": job.dealership.name
            }
        ]
        return context

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
            user = User.objects.get(email=user_email)
        else: 
            user = User.objects.create_user(user_email, full_name, "newpass123") # replace password with one time pass

        Job.objects.create(
            customer=user,
            customer_address=form.cleaned_data['customer_address'],
            contract_price=form.cleaned_data['contract_price'],
            seller=self.request.user,
            dealership=self.request.user.dealership,
            sale_date=datetime.datetime.now().date(),
            vin=form.cleaned_data['vin'],
            car_year=form.cleaned_data['car_year'],
            car_make=form.cleaned_data['car_make'],
            car_model=form.cleaned_data['car_model'],
            notes=form.cleaned_data['notes']
        )

        messages.add_message(
            self.request, messages.INFO, "Customer Info successfully updated and job started"
        )
        return super().form_valid(form)
      
job_creation_view = JobCreationView.as_view()

class PDFContractDetailView(PDFTemplateResponseMixin, DetailView):
    model = Job
    template_name = 'pdf/contract.html'

pdf_contract_detail_view = PDFContractDetailView.as_view()

class JobCustomerContacted(RedirectView): 
    def get_redirect_url(self, *args, **kwargs):
        job = Job.objects.get(id=kwargs['pk'])
        if job:
            job.customer_contacted = True
            job.save()
        return  reverse("dealers:job")

job_customer_contacted = JobCustomerContacted.as_view()
