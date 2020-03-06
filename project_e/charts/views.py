from project_e.jobs.models import Job
from project_e.jobs.views import JobCreationView
from project_e.dealers.views import DealerJobsView
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dealers/dealer_analytics.html', {"dealers": 10})

def get_data(self, *args, **kwargs):
    data = {
        "dealers": 10,
        "sales": 30,
    }
    response = JsonResponse(data)
    return response
        
home_view=HomeView.as_view()

class ChartData(APIView):
    template_name = "dealers/dealer_analytics.html"
    
    def get(self, request, format=None):
        counter = [0] * 13

        jobs = Job.objects.all()    
        if not self.request.user.is_staff:
            jobs = jobs.filter(dealership=self.request.user.dealership).order_by('sale_date')
        
        for e in jobs:
            counter[e.sale_date.month] += 1

        labels = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        default_items = counter[1:]

        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
        
chart_data_view=ChartData.as_view()