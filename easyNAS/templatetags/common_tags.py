from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.filter(name='jsonify')
def jsonify(list):
    return mark_safe(json.dumps(list))

@register.filter(name='split')
def split(value, arg):
	return value.split(arg)
