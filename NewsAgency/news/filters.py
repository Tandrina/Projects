# файл для создания фильтров через запрос (get)


from django_filters import FilterSet
from .models import Post


# создаем свой набор фильтров по категории сообщений
class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'headline': ['icontains'],
            'articleType': ['icontains'],
            'dateAdd': ['gt'],
        }
