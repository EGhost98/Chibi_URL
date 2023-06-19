from django.urls import path
from . import views

# app_name = "shortener"

urlpatterns = [
    # Home view
    path('', views.index, name='index'),
    path('<str:shortened_part>', views.redirect_url, name='redirect_url'),
]
