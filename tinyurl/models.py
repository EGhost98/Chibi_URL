from django.db import models
from .utils import create_shortened_url
from django.contrib.auth.models import User
from django.urls import reverse
# At the end of the  Shortener model

class Shortener(models.Model):
    '''
    Creates a short url based on the long one
    created -> Hour and date a shortener was created 
    times_followed -> Times the shortened link has been followed
    long_url -> The original link
    short_url ->  shortened link https://domain/(short_url)
    '''
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    url_index = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
    
    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            self.short_url = create_shortened_url(self) # We pass the model instance that is being saved
        super().save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("index", kwargs={"pk": self.pk})