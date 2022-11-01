from ast import Pass
from django.shortcuts import render, redirect
from . forms import  ArticleForm, ArticleAdminForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . models import Article
from django.contrib.auth.models import User
from . utils import get_article_count, get_article_count_per_user
from django.core.paginator import Paginator


# Create your views here.
def filter_my_articles(request, name):
    
    filter_txt = name.title()

    article_list = Article.objects.all().filter(category=filter_txt, author=request.user).order_by('-date_time')
    
        
    paginator = Paginator(article_list, per_page= 2)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    #getting number of articles for each category
    count_data = get_article_count_per_user(Article, request.user)
    last_article = Article.objects.all().filter(author=request.user).last()
    number_of_articles = Article.objects.all().filter(author=request.user).count()
    
    sport_count = count_data['sport_count']
    travel_count = count_data['travel_count']
    nature_count = count_data['nature_count'] 
    lifestyle_count = count_data['lifestyle_count']
    other_count = count_data['other_count']
    
    context = {
        'number_of_articles': number_of_articles,
        'last_article': last_article,
        'page_number': int(page_number),
        'paginator': paginator,
        'article_list': page_obj.object_list,
        'sport_count': sport_count,
        'travel_count':travel_count,
        'nature_count': nature_count,
        'lifestyle_count': lifestyle_count,
        'other_count': other_count,
    }
    
    return render(request,'articles/my_articles.html', context)



def filter_articles(request, name):
    
    filter_txt = name.title()

    article_list = Article.objects.all().filter(category=filter_txt).order_by('-date_time')
    all_articles = Article.objects.all().order_by('-date_time')
    latest_story_list = []
    for article in all_articles:
        latest_story_list.append(article)
        if len(latest_story_list) >= 3:
            break;
        
    paginator = Paginator(article_list, per_page= 2)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    #getting number of articles for each category
    count_data = get_article_count(Article)
    
    sport_count = count_data['sport_count']
    travel_count = count_data['travel_count']
    nature_count = count_data['nature_count'] 
    lifestyle_count = count_data['lifestyle_count']
    other_count = count_data['other_count']
    
    context = {
    
        'page_number': int(page_number),
        'paginator': paginator,
        'latest_stories': latest_story_list,
        'article_list': page_obj.object_list,
        'sport_count': sport_count,
        'travel_count':travel_count,
        'nature_count': nature_count,
        'lifestyle_count': lifestyle_count,
        'other_count': other_count,
    }
    
    return render(request,'articles/list_articles.html', context)

def search_my_article(request):
    if request.method == "POST":
        search = request.POST['search'].title()
       
        if len(search) < 9:
            article_list = Article.objects.all().filter(category=search, author=request.user).order_by('-date_time')
        else:
            article_list = Article.objects.all().filter(topic__startswith=search, author=request.user).order_by('-date_time')
        
        last_article = Article.objects.all().filter(author=request.user).last() 
        number_of_articles = Article.objects.all().filter(author=request.user).count()
        paginator = Paginator(article_list, per_page= 4)
        page_number = request.GET.get('page',1)
        page_obj = paginator.get_page(page_number)
        #getting number of articles for each category
        count_data = get_article_count_per_user(Article, request.user)
        sport_count = count_data['sport_count']
        travel_count = count_data['travel_count']
        nature_count = count_data['nature_count'] 
        lifestyle_count = count_data['lifestyle_count']
        other_count = count_data['other_count']
        
        context = {
            'number_of_articles': number_of_articles,
            'last_article': last_article,
            'page_number': int(page_number),
            'paginator': paginator,
            'article_list': page_obj.object_list,
            'sport_count': sport_count,
            'travel_count':travel_count,
            'nature_count': nature_count,
            'lifestyle_count': lifestyle_count,
            'other_count': other_count,
        }
        
        return render(request,'articles/my_articles.html', context)
    
        
       

def search_article(request):
    if request.method == "POST":
        search = request.POST['search'].title()
        print(search)
        if len(search) < 9:
            article_list = Article.objects.all().filter(category=search).order_by('-date_time')
        else:
            article_list = Article.objects.all().filter(topic__startswith=search).order_by('-date_time')
     
        paginator = Paginator(article_list, per_page= 2)
        page_number = request.GET.get('page',1)
        page_obj = paginator.get_page(page_number)
        #getting number of articles for each category
        count_data = get_article_count(Article)
        sport_count = count_data['sport_count']
        travel_count = count_data['travel_count']
        nature_count = count_data['nature_count'] 
        lifestyle_count = count_data['lifestyle_count']
        other_count = count_data['other_count']
        
        context = {
            'page_number': int(page_number),
            'paginator': paginator,
            'article_list': page_obj.object_list,
            'sport_count': sport_count,
            'travel_count':travel_count,
            'nature_count': nature_count,
            'lifestyle_count': lifestyle_count,
            'other_count': other_count,
        }
        
        return render(request,'articles/list_articles.html', context)
        
        
        
    
def delete_article(request, article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(id=article_id)
        if request.user == article.author or request.user.is_superuser:
            article.delete()
            return redirect('my_articles')
        else:
            messages.success(request, "Error! This article is not yours to delete")
            return redirect('home')
    else: 
        messages.success(request, "Error! You must be logged in to access this page")
        return redirect('home')
    


def edit_article(request,article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_id)
        if request.user == article.author or request.user.is_superuser:
            if request.method == "POST":
                if request.user.is_superuser:
                    form = ArticleAdminForm(request.POST or None, request.FILES or None, instance=article)              
                else:
                    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
                    
                if form.is_valid():
                    form.save()
                    messages.success(request, "Article updated successfully")
                    return redirect('my_articles')
                    
            else:
                if request.user.is_superuser:
                    form = ArticleAdminForm(request.POST or None, request.FILES or None, instance=article)
                else:
                    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
                context ={
                    'form': form
                }
                return render(request,'articles/edit_article.html',context)
        else:
            messages.success(request, "Error! you are logged in buy this article does not belong to you")
            return redirect('home')
    else: 
        messages.success(request, "You must be logged in to access this page")
        return redirect('home')

def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    category = article.category
    related_stories = []
    all_related_stories = Article.objects.filter(category=category).exclude(pk=article_id).order_by('-date_time')
    for story in all_related_stories:
        related_stories.append(story)
        if len(related_stories) >= 3:
            break
        
    #get text body as a list
    text_body_as_list = article.story.split('\n')
    
    
    
    
    context = {
        'article': article,
        'related_stories': related_stories,
        'text_body_as_list': text_body_as_list,

    }
    
    return render(request, 'articles/article.html', context)

def my_articles(request):
    if request.user.is_authenticated:
        user = request.user

        article_list = Article.objects.filter(author=user).order_by('-date_time')
        my_articles_count = article_list.count()
        count_data = get_article_count_per_user(Article, request.user)
        last_article = article_list.first()
        #getting number of articles for each category
        
        
        sport_count = count_data['sport_count']
        travel_count = count_data['travel_count']
        nature_count = count_data['nature_count'] 
        lifestyle_count = count_data['lifestyle_count']
        other_count = count_data['other_count']
        
        context = {
            'article_count': my_articles_count,
            'last_article': last_article,
            'article_list': article_list,
            'sport_count': sport_count,
            'travel_count': travel_count,
            'nature_count': nature_count,
            'lifestyle_count': lifestyle_count,
            'other_count': other_count,
            
        }
        
        return render(request, 'articles/my_articles.html', context)
    else:
        messages.success(request, "Youn must be logged in to access this page")
        return redirect('home')
    
    
    
def home(request):
    article_list = Article.objects.all().order_by('-date_time')
    latest_stories_list = []
    for article in article_list:
        latest_stories_list.append(article)
        if len(latest_stories_list) >= 5:
           break
    #getting number of articles for each category


    paginator = Paginator(article_list, per_page= 2)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    #getting number of articles for each category
    count_data = get_article_count(Article)
    sport_count = count_data['sport_count']
    travel_count = count_data['travel_count']
    nature_count = count_data['nature_count'] 
    lifestyle_count = count_data['lifestyle_count']
    other_count = count_data['other_count']
    
    context = {
        'latest_stories_list': latest_stories_list,
        'page_number': int(page_number),
        'paginator': paginator,
        'article_list': page_obj.object_list,
        'sport_count': sport_count,
        'travel_count':travel_count,
        'nature_count': nature_count,
        'lifestyle_count': lifestyle_count,
        'other_count': other_count,
    }
    return render(request, 'articles/home.html', context)




def list_articles(request):
    article_list = Article.objects.all().order_by('-date_time')
    latest_story_list = []
    for article in article_list:
        latest_story_list.append(article)
        if len(latest_story_list) >= 3:
            break;
    
    paginator = Paginator(article_list, per_page= 4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    #getting number of articles for each category
    count_data = get_article_count(Article)
    sport_count = count_data['sport_count']
    travel_count = count_data['travel_count']
    nature_count = count_data['nature_count'] 
    lifestyle_count = count_data['lifestyle_count']
    other_count = count_data['other_count']
    
    context = {
        'page_number': int(page_number),
        'paginator': paginator,
        'latest_stories': latest_story_list,
        'article_list': page_obj.object_list,
        'sport_count': sport_count,
        'travel_count':travel_count,
        'nature_count': nature_count,
        'lifestyle_count': lifestyle_count,
        'other_count': other_count,
    }
    
    return render(request, 'articles/list_articles.html', context)

def add_article(request):
    if request.user.is_authenticated:
        submitted = False
        if request.method == 'POST':
            if request.user.is_superuser:
                form = ArticleAdminForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Article added successfully")
                    return HttpResponseRedirect('/add_article?submitted=True')
            else:
                form = ArticleForm(request.POST, request.FILES)
                if form.is_valid():
                    article = form.save(commit=False)
                    article.author = request.user
                    article.save()
                    messages.success(request, "Article added successfully")
                    return HttpResponseRedirect('/add_article?submitted=True')
        
        else:
            if request.user.is_superuser:
                form = ArticleAdminForm
            
            else:
                form = ArticleForm
            
            if 'submitted' in request.GET:
                submitted = True
            
        context = {
            'form': form,
            'submitted':submitted
        }
        
        return render(request, 'articles/add_article.html', context)
        
            
    
    else:
        messages.success(request, "Error! You must be singed in before you add a new story")
        return redirect('home')

        
    
