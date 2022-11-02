from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    gender = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, blank=False, null=True, choices=gender)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    web_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username