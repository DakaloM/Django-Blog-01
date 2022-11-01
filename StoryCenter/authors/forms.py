from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        
class UpdateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'disabled':'true', 'readonly':'true'}), required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'disabled':'true', 'readonly':'true'}), required=False)
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2',
            )
        labels = {
            'username':'Usename',
            'email':'Email',
            'first_name':'First Name',
            'last_name':'Last Name',
            'password1':'Password',
            'password2':'Confirm Password'
            
        }
        
