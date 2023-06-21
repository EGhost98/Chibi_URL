from django.urls import path
from . import views

# app_name = "shortener"

urlpatterns = [
    path('', views.index.as_view(), name='index'),# Home view
    path('<str:shortened_part>', views.redirect_url, name='redirect_url'),
    path('a/my-urls',views.myurls, name='myurls'),
    path('delete/<int:id>',views.delete_item, name='delete_url'),
]

handler404 = views.handler404