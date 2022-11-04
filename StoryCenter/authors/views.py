from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import ProfileForm, UserForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from articles.models import Article
from . models import Profile
from . utils import progress_tracker

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
    
    
    user= User.objects.get(pk = user_id)
    instance, created = Profile.objects.get_or_create(user=user)
    article_count = Article.objects.all().filter(author=user).count()
    
    facebook_url = user.profile.facebook_url
    youtube_url = user.profile.youtube_url 
    twitter_url = user.profile.twitter_url
    web_url = user.profile.web_url
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST or None, instance= user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)

        
        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.bio = request.POST['bio']
            profile.gender = request.POST['gender']

            
            print("photo", profile.profile_image)
            user_form.save()
            profile.save() 
            
            return redirect('profile', user_id)
        
        context = {
            
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'authors/profile.html', context)
        
    else:
        user_form = UserUpdateForm(request.POST or None, instance=user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
        
        
        context = {
            'facebook_url': facebook_url,
            'youtube_url': youtube_url,
            'twitter_url': twitter_url,
            'web_url' : web_url,
            'profile_user': user,
            'logged_user_id': user_id,
            'sport_progress': progress_tracker(Article,user, "Sport"),
            'travel_progress': progress_tracker(Article,user,  "Travel"),
            'nature_progress': progress_tracker(Article,user,  "Nature"),
            'lifestyle_progress': progress_tracker(Article,user,  "Lifestyle"),
            'other_progress': progress_tracker(Article,user,  "Other"),
            'article_count': article_count,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        
        return render(request, 'authors/profile.html', context)
 

