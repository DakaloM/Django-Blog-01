from django.contrib import admin
from . models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('category', 'author', 'date_time', 'topic','intro','story','story_image')
    list_display = ('category', 'author', 'date_time', 'topic','intro','story','story_image')
    ordering = ('topic',)