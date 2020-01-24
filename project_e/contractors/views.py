from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from project_e.contractors.forms import ContractorCreationForm
from project_e.contractors.models import Contractor


class ContractorCreationView(CreateView): 
    model = Contractor
    fields = ["cont_name", "cont_email", "fname", "lname", "phone", "address"]

class ContractorDetailView(LoginRequiredMixin, DetailView):
    model = Contractor

contractor_detail_view = ContractorDetailView.as_view()
contractor_creation_view = ContractorCreationView.as_view()

