# coding=utf-8
from django import template

register = template.Library()

@register.simple_tag
def widget_color(dictionary, *args, **kwargs):
    total = kwargs['total']
    level = kwargs['current']
    return '/static/img/single-' + str(total) + '-' + dictionary.get(total)[level] + '.png'