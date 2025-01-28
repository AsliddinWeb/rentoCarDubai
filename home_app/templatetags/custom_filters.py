from django import template

register = template.Library()

@register.filter
def repeat(value, count):
    """Generates a list with the value repeated 'count' times."""
    return [value] * count

@register.filter
def subtract(value, arg):
    """Subtracts arg from value and returns the result."""
    return value - arg
