from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'profile_page': True
    }

    return render(request, template, context)

def personal_details(request):
    """ Users details and update """

    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details was successsfully updated')
        else:
            messages.error(request, 'Update failed. Please check all details are correst and try again.')
    else:
        form = ProfileForm(instance=profile)

    template = 'profiles/personal_details.html'
    context = {
        'form': form,
        'profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/success_checkout.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)