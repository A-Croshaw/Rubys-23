from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):

    return price * quantity

@register.filter(name='calc_subtotal_used')
def calc_subtotal_used(price, quantity):

    return Decimal(price / 2) * quantity
    
@register.filter(name='calc_used_price')
def calc_used_price(price):

    return Decimal(price / 2)
