from django.urls import path
from project_e.jobs.views import (
    job_creation_view, 
    job_detail_view
)

app_name = "jobs"
urlpatterns = [
    path("create/", view=job_creation_view, name="create"),
    path("<int:id>/", view=job_detail_view, name="detail")
]
