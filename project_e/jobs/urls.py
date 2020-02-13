from django.urls import path
from project_e.jobs.views import (
    job_creation_view, 
    pdf_contract_detail_view
    job_detail_view, 
    job_customer_contacted
)

app_name = "jobs"
urlpatterns = [
    path("create/", view=job_creation_view, name="create"),
    path("<int:pk>/", view=job_detail_view, name="detail"),
    path("pdf/<int:pk>/", view=pdf_contract_detail_view, name="pdf")
    path("contacted/<int:pk>/", view=job_customer_contacted, name="contacted")
]
