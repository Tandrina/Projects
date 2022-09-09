from datetime import datetime

from django import template

register = template.Library()


def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
        return d.urlendcode()
