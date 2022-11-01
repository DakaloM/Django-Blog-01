from django import forms
from django.forms import ModelForm
from . models import Article

class ArticleAdminForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ('category', 'author', 'date_time', 'topic', 'intro','story','story_image')
        
        labels = {
            'category': 'Category',
            'author': 'Author',
            'date_time': '',
            'topic': '',
            'intro': '',
            'story': '',
            'story_image': 'Image',
        }
        
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Topic'}),
            'intro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduction'}),
            'story': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Story'}),
        }
        
   
class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('category', 'date_time', 'topic', 'intro','story','story_image')
        
        labels = {
            'category': 'Category',
            'date_time': 'Date: (YYYY-MM-DD HH:MM)',
            'topic': 'Topic',
            'intro': 'Introduction',
            'story': 'Story',
            'story_image': 'Image',
        }
        
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Topic'}),
            'intro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduction'}),
            'story': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Story'}),
        }
    
   
