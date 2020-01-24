from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import UserView, signup
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
    path("<int:id>/", view=user_detail_view, name="detail"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('profile/',  login_required(UserView.as_view()), name='profile'),
    path('signup/', signup, name='signup')
]
