from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt decorator
from . import views

urlpatterns = [
    path('login/', csrf_exempt(auth_views.LoginView.as_view(template_name='users/login.html', extra_context={'show_welcome_notification': True})), name='login'),
    path('logout/', csrf_exempt(auth_views.LogoutView.as_view()), name='logout'),
    path('register/', csrf_exempt(views.register), name='register'),
]
