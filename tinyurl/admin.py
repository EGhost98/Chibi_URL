from django.contrib import admin
from .models import Shortener
# Register your models here.
admin.site.site_header = "URL_Shortener Admininstration"
admin.site.site_title = "URL_Shortener"
admin.site.index_title = "Manage URL Shortener"

class TinyAdmin(admin.ModelAdmin):
    
    list_display = ('created','long_url','short_url',)
    search_fields = ('long_url',)


admin.site.register(Shortener,TinyAdmin)