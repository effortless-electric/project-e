from django.urls import path

from project_e.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_add_dealer_view,
    user_add_customer_view,
    user_verify_view,
    user_remove_view
)

app_name = "users"
urlpatterns = [
    path("add-dealer/<str:ref_id>", view=user_add_dealer_view, name="add-dealer"),
    path("add-customer/", view=user_add_customer_view, name="add-customer"),
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("verify/<int:user_id>", view=user_verify_view, name="verify"),
    path("remove/<int:user_id>", view=user_remove_view, name="remove"),
    path("<str:username>/", view=user_detail_view, name="detail")
]
