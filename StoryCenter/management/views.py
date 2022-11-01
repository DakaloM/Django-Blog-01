from django.shortcuts import render, redirect
from articles.models import Article
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def admin(request, user_id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            article_list = Article.objects.all()
            user_list = User.objects.all()
            
            #get number of superusers
            superuser_list = []
            for user in user_list:
                if user.is_staff:
                    superuser_list.append(user)
                else:
                    continue
            
            number_of_articles = article_list.count()
            number_of_authors = user_list.count()
            number_of_staff = len(superuser_list)
            
            context = {
                'article_list': article_list,
                'user_list': user_list,
                'superuser_list': superuser_list,
                'number_of_articles': number_of_articles,
                'number_of_authors': number_of_authors,
                'number_of_staff': number_of_staff,
            }
            return render(request,'management/admin.html', context)
        else:
            messages.success(request, "Error! You are not authorized to access this page")
            return redirect('home')
            
    else: 
        messages.success(request, "Error! You must be logged in to access this page")
        return redirect('home')

def user_articles(request, user_id):
    
    user = User.objects.get(pk=user_id)
    article_list = Article.objects.all().filter(author=user)
    number_of_articles = article_list.count()

    context = {
        
        'user': user,
        'article_list': article_list,
        'number_of_articles': number_of_articles,
    }
    return render(request,'management/user_articles.html' , context)

def delete_article(request, article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(id=article_id)
        author = article.author
        if request.user == article.author or request.user.is_superuser:
            article.delete()
            return redirect('user_articles', author.id)
        else:
            messages.success(request, "Error! This article is not yours to delete")
            return redirect('home')
    else: 
        messages.success(request, "Error! You must be logged in to access this page")
        return redirect('home')
    
    
def delete_article_admin(request, article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(id=article_id)
        author = article.author
        if request.user == article.author or request.user.is_superuser:
            article.delete()
            return redirect('admin', request.user.id)
        else:
            messages.success(request, "Error! This article is not yours to delete")
            return redirect('home')
    else: 
        messages.success(request, "Error! You must be logged in to access this page")
        return redirect('home')
    
def demote(request, user_id):
    
    if request.user.is_authenticated and request.user.is_superuser:
        admin_id = request.user.id
        all_users = User.objects.all()
        staff_users = []
        for user in all_users:
            if user.is_staff:
                staff_users.append(user)
        
        user = User.objects.get(pk=user_id)
        if len(staff_users) > 1:
            user.is_staff = False
            user.save()
            message = user.username + " Demoted from Staff!" 
            messages.success(request, message)
            return redirect('admin',admin_id)
        else:
            messages.success(request, "Error! There must be at least one staff member available")
            return redirect('admin',admin_id)
    else: 
        messages.success(request, "Error! Action unauthorized!")
        return redirect('home')


def promote(request, user_id):
    if request.user.is_authenticated and request.user.is_superuser:
        admin_id = request.user.id
        user = User.objects.get(pk=user_id)
        user.is_staff = True
        user.save()
        message = user.username + " promoted to Staff!" 
        messages.success(request, message)
        return redirect('admin',admin_id)
    else: 
        messages.success(request, "Error! Action unauthorized!")
        return redirect('home')

def delete_user(request, user_id):
    if request.user.is_authenticated and request.user.is_superuser:
        admin_id = request.user.id
        user = User.objects.get(pk=user_id)
        user.delete()
        message = user.username + " Is Deleted" 
        messages.success(request, message)
        return redirect('admin',admin_id)
    else: 
        messages.success(request, "Error! Action unauthorized!")
        return redirect('home')

