from django.urls import path

from project_e.contractors.views import (
    contractor_creation_view,
    contractor_detail_view
)

app_name = "contractors"
urlpatterns = [
    path("create/", view=contractor_creation_view, name="create"),
    path("<int:pk>/", view=contractor_detail_view, name="detail")
]
