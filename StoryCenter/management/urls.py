from django.urls import path
from . import views

urlpatterns = [
    path('admin_area/<user_id>', views.admin, name='admin'),
    path('user_articles/<user_id>', views.user_articles, name='user_articles'),
    path('demote/<user_id>', views.demote, name='demote'),
    path('promote/<user_id>', views.promote, name='promote'),
    path('delete_user/<user_id>', views.delete_user, name='delete_user'),
    path('admin_delete_article/<article_id>', views.delete_article, name='admin_delete_article'),
    path('delete_article_admin/<article_id>', views.delete_article_admin, name='delete_article_admin'),
]
