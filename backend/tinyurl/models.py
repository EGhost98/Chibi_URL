from django.db import models
from .utils import create_shortened_url
from django.contrib.auth.models import User

class Shortener(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField(max_length = 500)
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    url_index = models.CharField(max_length=100, blank=True)
    url_alias = models.CharField(max_length=15, blank=True)
    
    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=['url_index'], name='index'),
            models.Index(fields=['url_alias'], name='alias'),
            models.Index(fields=['short_url'], name='short_url'),
            models.Index(fields=['user_name'], name='user_name'),
        ]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
    
    def save(self, *args, **kwargs):
        if not self.short_url:  
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)