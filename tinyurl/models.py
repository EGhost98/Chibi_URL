from django.db import models
from .utils import create_shortened_url
from django.contrib.auth.models import User

class Shortener(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1) # user cuurrently logged in to associate url
    created = models.DateTimeField(auto_now_add=True) # Hour and date a shortener was created 
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField() #The original link
    short_url = models.CharField(max_length=15, unique=True, blank=True) # shortened link https://domain/(short_url)
    url_index = models.CharField(max_length=100, blank=True) # index a url by giving it a custom name

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
    
    def save(self, *args, **kwargs):
        if not self.short_url:  # If the short url wasn't specified
            self.short_url = create_shortened_url(self) # We pass the model instance that is being saved
        super().save(*args, **kwargs)