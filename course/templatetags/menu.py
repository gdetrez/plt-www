from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def active(request, name):
    path = request.path
    print reverse(name)
    if path.startswith(pattern):
        return True
    return False
