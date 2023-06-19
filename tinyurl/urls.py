from django.urls import path
from . import views

# app_name = "shortener"

urlpatterns = [
    # Home view
    path('', views.index.as_view(), name='index'),
    path('<str:shortened_part>', views.redirect_url, name='redirect_url'),
    path('a/my-urls',views.myurls, name='myurls'),
]
