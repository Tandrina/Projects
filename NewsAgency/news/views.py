from _datetime import datetime

from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post


class PostsLIst(ListView):
    model = Post  # какую модель используем
    ordering = '-dateAdd'  # по какому полю пойдет сортировка
    template_name = 'articles.html'  # шаблон для отображения
    context_object_name = 'posts'  # список объектов, которые будут передаваться в шаблон

    def get_context_data(self, **kwargs):
        # обращаемся к родительскому классу
        # и вызываем этот же метод с теми же аргументами,
        # что были переданы нам.
        context = super().get_context_data(**kwargs)
        # К словарю добавляем текущую дату с ключом 'time_now'
        context['time_now'] = datetime.utcnow()
        # Добавляем пустую переменную для создания фильтра в дальнейшем
        context['news_length'] = None
        return context


class PostsDetails(DetailView):
    model = Post
    ordering = 'dateAdd'
    template_name = 'post.html'
    context_object_name = 'post'
