from django.urls import path

from project_e.charts.views import(home_view, get_data, chart_data_view)

from project_e.dealers.views import (
    dealer_creation_view, 
    dealer_detail_view, 
    dealer_user_verify_view,
    dealer_analytics_view,
    dealer_user_verify_view, 
    dealer_jobs_view, 
    dealer_employee_detail, 
    dealer_create_employee,
    staff_dealer_creation_view
)

app_name = "dealers"
urlpatterns = [
    path("create/", view=dealer_creation_view, name="create"),
    path("<int:pk>/", view=dealer_detail_view, name="detail"),
    path("verify/", view=dealer_user_verify_view, name="verify"),
    path("analytics/", view=dealer_analytics_view, name="analytics"),
    path("jobs/", view=dealer_jobs_view, name="job"), 
    path("sales/<int:pk>", view=dealer_employee_detail, name="employee-detail"), 
    path("new-associate/", view=dealer_create_employee, name="employee-create"),
    path("analytics/", view=home_view, name="analytics"),
    path("analytics/api/chart/data", view=chart_data_view),
    path("sales/<int:pk>", view=dealer_employee_detail, name="employee-detail"),
    path("new-associate/", view=dealer_create_employee, name="employee-create"),
    path("dealer-creation-portal/", view=staff_dealer_creation_view, name="creation-portal")
]
