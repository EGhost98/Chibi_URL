from django.contrib import admin
from .models import Shortener
# Register your models here.
admin.site.site_header = "URL_Shortener Admininstration"
admin.site.site_title = "URL_Shortener"
admin.site.index_title = "Manage URL Shortener"

class TinyAdmin(admin.ModelAdmin):
    
    list_display = ('user_name','created','url_index','short_url','long_url',)
    search_fields = ('long_url','url_index',)


admin.site.register(Shortener,TinyAdmin,)