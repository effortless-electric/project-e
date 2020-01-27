from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib import messages

from project_e.dealers.models import Dealer
from project_e.dealers.forms import EmployeeCreationForm
from project_e.customers.models import Customer
from project_e.jobs.models import Job

User = get_user_model()


class DealerCreationView(CreateView):
    model = Dealer
    fields = ["name", "address"]

    def form_valid(self, form):
        form.instance.admin = self.request.user
        self.request.user.sales = True
        self.request.user.verified = True
        self.request.user.save(update_fields=["sales", "verified"])
        return super().form_valid(form)

    def get_success_url(self):
        self.request.user.dealership = self.object
        self.request.user.save(update_fields=["dealership"])
        return self.request.user.get_absolute_url()

class DealerVerifyView(LoginRequiredMixin, ListView):
    queryset = User.objects.all()
    template_name = 'dealers/dealer_employees.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DealerVerifyView, self).get_context_data(*args, **kwargs)
        context['url'] = self.request.build_absolute_uri(reverse('users:add-dealer', kwargs={'ref_id':self.request.user.dealership.ref_id}))
        context['verified'] = context["user_list"].filter(verified=True)
        context['unverified'] = context["user_list"].filter(verified=False)
        return context

    def get_queryset(self):
        dealer = self.request.user.dealership
        return User.objects.filter(dealership=dealer)

class DealerDetailView(LoginRequiredMixin, DetailView):
    model = Dealer

class DealerAddCustView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ["cust_email", "cust_address", "fname", "lname", "phone", "vin", "car_make", "car_model"]

class DealerJobsView(LoginRequiredMixin, ListView): 
    queryset = Job.objects.all()
    template_name = 'dealers/dealer_jobs.html'

    def get_context_data(self, *args, **kwargs): 
        context = super(DealerJobsView, self).get_context_data(*args, **kwargs)
        context['jobs'] = Job.objects.filter(dealership=self.request.user.dealership)
        return context

class DealerEmployeeView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "dealers/dealer_employee_detail.html"

    def get_context_data(self, *args, **kwargs): 
        context = super(DealerEmployeeView, self).get_context_data(*args, **kwargs)
        salesman = kwargs['object']
        context['jobs'] = Job.objects.filter(seller=salesman)
        return context

class DealerCreateEmployeeView(LoginRequiredMixin, FormView): 
    model = User
    template_name = "dealers/employee_creation_form.html"
    form_class = EmployeeCreationForm

    def get_success_url(self): 
        return reverse("dealers:verify")

    def form_valid(self, form): 
        full_name = form.cleaned_data["first_name"] + ' ' + form.cleaned_data["last_name"]
        user_email = form.cleaned_data["email"]
        user = User.objects.filter(email=user_email)
        if user:
            user = User.objects.get(email=user_email) 
        else:
            user = User.objects.create_user(user_email, full_name, "testaccount")
        user.dealership = self.request.user.dealership
        user.sales = True
        user.save()

        user.send_reset_email(self.request)
        
        messages.add_message(
            self.request, messages.INFO, "Associate Created Successfully"
        )
        return super().form_valid(form)

dealer_user_verify_view = DealerVerifyView.as_view()
dealer_detail_view = DealerDetailView.as_view()
dealer_creation_view = DealerCreationView.as_view()
dealer_addcust_view = DealerAddCustView.as_view()
dealer_jobs_view = DealerJobsView.as_view()
dealer_employee_detail = DealerEmployeeView.as_view()
dealer_create_employee = DealerCreateEmployeeView.as_view()
