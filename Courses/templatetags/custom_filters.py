from django.template import Library

register = Library()


@register.filter
def lookup(d, key):
    # simple access here, you can also raise exception in case key is not found
    return d.get(key)
