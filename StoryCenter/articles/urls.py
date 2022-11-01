from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<article_id>', views.edit_article, name='edit_article'),
    path('article/<article_id>/', views.article, name='article'),
    path('list_articles/', views.list_articles, name='list_articles'),
    path('my_articles/', views.my_articles, name='my_articles'),
    path('search/', views.search_article, name='search'),
     path('search_me/', views.search_my_article, name='search_me'),
    path('filter_list/<str:name>', views.filter_articles, name='filter_articles'),
    path('filter_me/<str:name>', views.filter_my_articles, name='filter_me'),
    path('delete_article/<article_id>', views.delete_article, name='delete_article'),
    
]
