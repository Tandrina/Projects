from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsLIst.as_view(), name='post_list'),
    path('<int:pk>', PostsDetails.as_view(), name='post_detail'),
    path('search/', SearchLIst.as_view(), name='search_form'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDel.as_view(), name='news_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDel.as_view(), name='article_delete'),
]
