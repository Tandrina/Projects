from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import *


class PostsLIst(ListView):
    model = Post  # какую модель используем
    ordering = '-dateAdd'  # по какому полю пойдет сортировка
    template_name = 'articles.html'  # шаблон для отображения
    context_object_name = 'posts'  # список объектов, которые будут передаваться в шаблон
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # обращаемся к родительскому классу
        # и вызываем этот же метод с теми же аргументами,
        # что были переданы нам.
        context = super().get_context_data(**kwargs)
        # К словарю добавляем текущую дату с ключом 'time_now'
        context['time_now'] = datetime.utcnow()  # создаем переменную time_now
        context['filterset'] = self.filterset  # создаем переменную filterset с данным из запроса
        return context


class SearchLIst(ListView):
    model = Post  # какую модель используем
    ordering = '-dateAdd'  # по какому полю пойдет сортировка
    template_name = 'search.html'  # шаблон для отображения
    context_object_name = 'posts'  # список объектов, которые будут передаваться в шаблон
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # обращаемся к родительскому классу
        # и вызываем этот же метод с теми же аргументами,
        # что были переданы нам.
        context = super().get_context_data(**kwargs)
        # К словарю добавляем текущую дату с ключом 'time_now'
        context['time_now'] = datetime.utcnow()  # создаем переменную time_now
        context['filterset'] = self.filterset  # создаем переменную filterset с данным из запроса
        return context


class PostsDetails(DetailView):
    model = Post
    ordering = 'dateAdd'
    template_name = 'post.html'
    context_object_name = 'post'


# Создаем представление для отображения страницы создания новости
class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.articleType = 'NW'
        return super().form_valid(form)


# Создаем представление для отображения страницы модерации новости
class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_update.html'


# Создаем представление для отображения страницы удаления новости
class NewsDel(DeleteView):
    form_class = NewsForm
    model = Post
    template_name = 'news_delete.html'


# Создаем представление для отображения страницы создания статьи
class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'art_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.articleType = 'AR'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'art_update.html'


class ArticleDel(DeleteView):
    form_class = NewsForm
    model = Post
    template_name = 'art_delete.html'
