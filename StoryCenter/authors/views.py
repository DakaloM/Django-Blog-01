from django.shortcuts import render, redirect, reverse
from . forms import UserForm,  UpdateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login successfully')
            return redirect('home')
        else:
            messages.success(request, 'Error!, Login failed, Invalid useraname or password')
            return redirect('login')
    else:
        return render(request, 'authors/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, 'Success, you have logged out')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save();
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
           
            messages.success(request, 'Registration successfully, You are loged in')
            return redirect('home') 
    else:
        form = UserForm()
        
    context = {'form': form}
    return render(request, 'authors/register.html', context)

def user_profile(request,user_id):
    author = User.objects.get(pk=user_id)
    context = {'author':author}
    return render(request, 'authors/profile.html', context)

