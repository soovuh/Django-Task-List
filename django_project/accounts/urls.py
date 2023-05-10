from django.urls import path, include, re_path as url
from django.contrib.auth import views as auth_views

from . import views
from .forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html',
                                     authentication_form=CustomAuthenticationForm),
        name='login'),
    path('logout/', views.logout_view, name='logout'),
]
