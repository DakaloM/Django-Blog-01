from django.contrib import admin
from . models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    fields = (
        'user', 'bio','gender', 'profile_image', 'facebook_url',
        'twitter_url', 'youtube_url', 'web_url'
    )
    
    list_display = (
        'user', 'bio','gender', 'profile_image',  'facebook_url',
        'twitter_url', 'youtube_url', 'web_url'
    )