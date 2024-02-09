from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def shopping_items(request):
    """ Creates shopping items with price calculations"""
    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})
    delivery = 0

    for item_id, quantity in cart.items():
        book = get_object_or_404(Book, pk=item_id)
        if book.condition == "used":
            price_used = Decimal(book.price / 2)
            total += quantity * price_used
            item_count += quantity

            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'book': book,
                'price_used':price_used,
            })
        else:
            total += quantity * book.price
            item_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'book': book,
            })
    
    if total > 0:
         delivery = settings.STANDARD_DELIVERY
    if total < settings.FREE_DELIVERY:
        delivery_difference = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        delivery_difference = 0
    
    overal_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'delivery_difference': delivery_difference,
        'free_delivery': settings.FREE_DELIVERY,
        'overal_total': overal_total,
    }

    return context