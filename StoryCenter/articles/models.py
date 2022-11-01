from random import choices
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

    
class Article(models.Model):
    CATEGOTY = (
        ('Sport', 'Sport'),
        ('Nature', 'Nature'),
        ('Travel', 'Travel'),
        ('Lifestyle', 'Lifestyle'),
        ('Other', 'Other'),
    )
    category = models.CharField(max_length=255, blank=False, null=False,choices=CATEGOTY)
    author =  models.ForeignKey(User,blank=False, null=False ,on_delete=models.CASCADE)
    date_time= models.DateTimeField(default=datetime.datetime.now)
    topic = models.CharField(max_length=100, blank=False, null=False)
    intro = models.CharField(max_length=255, blank=False, null=False)
    story = models.TextField(blank=False, null=False)
    story_image = models.ImageField(null=False, blank=False, upload_to='images/')
    
    def __str__(self):
        return self.topic