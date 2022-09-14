# файл для создания фильтров через запрос (get)
import django_filters
from django.forms import DateInput, TextInput
from .models import Post


# создаем свой набор фильтров по категории сообщений
class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='headline',
        lookup_expr='icontains',
        widget=TextInput(attrs={'type': 'text'}),
        label='Название статьи',
    )

    type = django_filters.CharFilter(
        field_name='articleType',
        lookup_expr='icontains',
        widget=TextInput(attrs={'type': 'text'}),
        label='Тип статьи',
        # empty_label='Дата статьи'
    )

    date_after = django_filters.DateFilter(
        field_name='dateAdd',
        lookup_expr='gt',
        widget=DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'},
        ),
        label='Тип статьи',
    )
