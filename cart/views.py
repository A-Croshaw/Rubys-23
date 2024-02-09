from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from books.models import Book


def shopping_cart(request):
    """ View that renders the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adding books to shopping cart with quantities"""
    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
         cart[item_id] += quantity
         price_sub = book.price * quantity
         messages.success(request, f'{cart[item_id]} x {book.title} added to cart')
    else:
         cart[item_id] = quantity
         price_sub = book.price * quantity
         messages.success(request, f'{cart[item_id]} x {book.title} added to cart')
    
    request.session['cart'] = cart

    return redirect(redirect_url,)


def update_cart(request, item_id):
    """Adjusting book quantities"""

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {book.title} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {book.title} from the shopping cart')

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def remove_item(request, item_id):
    """Remove items from the cart"""

    try:
        book = get_object_or_404(Book, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {book.title} from the shopping cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
