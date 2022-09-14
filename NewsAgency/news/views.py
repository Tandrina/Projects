from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter
from django.http import HttpResponse


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

# def search_news(request):
#     return HttpResponse(render(request, 'search.html'))
