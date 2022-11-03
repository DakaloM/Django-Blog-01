from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import Profile

class UserUpdateForm(UserChangeForm):
    
    
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name' ,
            )
        labels = {
            'username':'',
            'email':'',
            'first_name':'',
            'last_name':'',
          
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }
    
class UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2',
            )
        labels = {
            'username':'',
            'email':'',
            'first_name':'',
            'last_name':'',
            'password1':'',
            'password2':''
            
        }
        
class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = (
                'facebook_url','twitter_url','youtube_url','web_url','profile_image' 
            )
        labels = {
            'gender':'Gender',
            'bio':'',
            'facebook_url':'',
            'twitter_url':'',
            'youtube_url':'',
            'web_url':'',
            
            
        }
        
        widgets = {
            'gender': forms.Select(attrs={
                    'class': 'form-control', 'placeholder': 'Gender',
                }),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook URL'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Twitter Link'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Youtube link'}),
            'web_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website Link'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'inputGroupFile02'
                }),
        }
        
        
