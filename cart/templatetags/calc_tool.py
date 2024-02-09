from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):

    return price * quantity

@register.filter(name='calc_subtotal_used')
def calc_subtotal_used(price_used, quantity):

    return price_used * quantity