from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, name):
    current_path = context['request'].get_full_path()
    url_path = reverse(name)
    if current_path.startswith(url_path):
        return True
    return False

@register.simple_tag(takes_context=True)
def menuitem(context, name, title):
    current_path = context['request'].get_full_path()
    url_path = reverse(name)
    cssclass = ""
    if current_path.startswith(url_path):
        cssclass = "active"
    return "<li class=\"%s\"><a href=\"%s\">%s</a></li>" % (cssclass,url_path,title)
