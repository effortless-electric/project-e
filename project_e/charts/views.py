from project_e.jobs.models import Job
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
    
    def get(self, request, format=None):
        

        labels = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec  "]
        default_items = [1, 3, 3, 7, 17, 20, 20, 29, 20, 18, 
                        22, 23]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
chart_data_view=ChartData.as_view()