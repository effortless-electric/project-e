from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from project_e.dealers.models import Dealer
from project_e.customers.models import Customer

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
        return super(DealerCreationView, self).get_success_url()

class DealerVerifyView(LoginRequiredMixin, ListView):
    queryset = User.objects.all()

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


dealer_user_verify_view = DealerVerifyView.as_view()
dealer_detail_view = DealerDetailView.as_view()
dealer_creation_view = DealerCreationView.as_view()
dealer_addcust_view = DealerAddCustView.as_view()
