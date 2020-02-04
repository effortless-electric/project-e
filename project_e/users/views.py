from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView, FormView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from project_e.dealers.models import Dealer
from project_e.dealers.views import dealer_analytics_view

from project_e.users.models import User


from project_e.contractors.models import Contractor
from project_e.contractors.forms import ContractorCreationForm

from project_e.customers.models import Customer
from project_e.customers.forms import DealerAddCustForm

from project_e.jobs.models import Job

from .forms import SignUpForm

#from project_e.jobs.models import Job
#from project_e.jobs.forms import Form

User = get_user_model()

class UserView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "id"
    slug_url_kwarg = "id"

    def get(self, *args, **kwargs):
        template_name = "users/user_detail.html"
        if self.request.user.dealership or self.request.user.is_staff: 
            return dealer_analytics_view(self.request)
        return render(self.request, template_name, kwargs)
            
user_detail_view = UserDetailView.as_view()

class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["dealership"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"id": self.request.user.id})

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"id": self.request.user.id})


user_redirect_view = UserRedirectView.as_view()

class UserAddContractorView(LoginRequiredMixin, FormView):
    model = Contractor
    fields = ["cont_name", "cont_email", "fname", "lname", "phone", "address"]
    template_name = "users/createcont_form.html"
    form_class = ContractorCreationForm
    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        # if (not Contractor.objects.get(id=self.request.contractor)):
        #     return False
        form.save()
        messages.add_message(
            self.request, messages.INFO, _("Thanks! Your contractor info was successfully updated")
        )
        return super().form_valid(form)

user_add_contractor_view = UserAddContractorView.as_view()

class UserAddDealerView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        dealer = Dealer.objects.get(ref_id=kwargs['ref_id'])
        self.request.user.dealership = dealer
        self.request.user.sales = True
        self.request.user.verified = False
        self.request.user.save(update_fields=['dealership', 'sales', 'verified'])
        return reverse("users:detail", kwargs={"id": self.request.user.id})

user_add_dealer_view = UserAddDealerView.as_view()

class UserVerifyView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        if user:
            user.verified = not user.verified
            user.save(update_fields=['verified'])
        return  reverse("dealers:employee-detail", kwargs={"pk": user.id})
user_verify_view = UserVerifyView.as_view()

class UserRemoveView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(id=kwargs["user_id"])
        user.dealership = None
        user.verified = False
        user.sales = False
        user.save(update_fields=["dealership", "verified", "sales"])
        return reverse("dealers:verify")
user_remove_view = UserRemoveView.as_view()

class UserConfirmRemoveView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "dealers/dealers_confirm_remove.html"

user_confirm_remove_view = UserConfirmRemoveView.as_view()