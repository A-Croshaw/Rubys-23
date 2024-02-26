from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def cart_contents(request):
    """ Creates shopping items with price calculations"""
    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            book = get_object_or_404(Book, pk=item_id)
            if book.condition == "used":
                total += item_data * Decimal(book.price / 2)
            else:
                total += item_data * book.price
            item_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'book': book,
            })
    if total < settings.FREE_DELIVERY:
        delivery = settings.STANDARD_DELIVERY
        delivery_difference = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        delivery_difference = 0
    
    if total > 0:
        overal_total = delivery + total
    else:
        overal_total = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'delivery_difference': delivery_difference,
        'free_delivery': settings.FREE_DELIVERY,
        'standard_delivery': settings.STANDARD_DELIVERY,
        'overal_total': overal_total,
    }

    return context