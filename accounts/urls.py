from django.urls import path
from accounts.views import UserRegistrationView, activate
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    ]