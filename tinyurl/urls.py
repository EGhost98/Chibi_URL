from django.urls import path
from . import views

# app_name = "shortener"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),# Home view
    path('about',views.about, name='about'),
    path('a/my-urls',views.myurls, name='myurls'),
    path('delete/<int:id>',views.delete_item, name='delete_url'),
    path('<str:shortened_part>', views.redirect_url, name='redirect_url'),
]

handler404 = views.handler404