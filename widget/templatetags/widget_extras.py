# coding=utf-8
from django import template

register = template.Library()

@register.simple_tag
def widget_color(dictionary, *args, **kwargs):
    total = kwargs['total']
    level = kwargs['current']
    return 'img/single-' + str(total) + '-' + dictionary.get(total)[level - 1] + '.png'