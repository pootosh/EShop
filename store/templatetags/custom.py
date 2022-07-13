from django import template

register = template.Library()

@register.filter(name='custom_currency')
def custom_currency(price):
    return '₹'+str(price)