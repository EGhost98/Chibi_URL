from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tinyurl import views as tinyurl_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('users.urls')),
    path('', include('tinyurl.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = tinyurl_views.handler404