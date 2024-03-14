from django.shortcuts import get_object_or_404, reverse, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import (
    login_required, permission_required)
from . forms import SubscribersForm, NewslettersForm
from . models import Subscribers, Newsletters
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
import datetime


def subscribe(request):
    """ A view to return the subscribe page """
    newsletter = Newsletters.objects.all()

    today = datetime.date.today().month
    year = datetime.date.today().year

    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return HttpResponseRedirect('../subscribe')
    else:
        form = SubscribersForm()
    context = {
        'form': form,
        'newsletter': newsletter,
        'year': year,
        'today': today,
    }
    return render(request, 'newsletter/subscribe.html', context)


@login_required
@permission_required("newsletter.newsletters", raise_exception=True)
def newsletters(request):
    """
    A view to render all newsletterss with searching functions
    """
    newsletter = Newsletters.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No newsletters with that criteria")
                return redirect(reverse('newsletters'))

            queries = Q(title__icontains=query)
            newsletter = newsletter.filter(queries)

    context = {
        'newsletter': newsletter,
    }

    return render(request, 'newsletter/newsletter.html', context)


@login_required
@permission_required("newsletter.newsletter_view", raise_exception=True)
def newsletter_view(request, newsletter_id):
    """ View to see full book """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users can only access newsletters.')
        return redirect(reverse('home'))

    newsletter = get_object_or_404(Newsletters, pk=newsletter_id)

    context = {
        'newsletter': newsletter,
    }

    return render(request, 'newsletter/newsletter_view.html', context)


@login_required
@permission_required("newsletter.new_newsletter", raise_exception=True)
def new_newsletter(request):
    """ Create a new newsletter """
    emails = Subscribers.objects.all()
    s_list = read_frame(emails, fieldnames=['email'])
    subscriber_list = s_list['email'].values.tolist()
    print(subscriber_list)

    if not request.user.is_superuser:
        messages.error(request, 'Admin users can only create newsletters.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewslettersForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                subscriber_list,
                fail_silently=False,
            )
            messages.success(
                request, 'Montly newsletter has been sent successfully')
            return redirect('newsletters')
    else:
        form = NewslettersForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/new_newsletter.html', context)


@login_required
@permission_required("newsletter.newsletter_delete", raise_exception=True)
def newsletter_delete(request, newsletter_id):
    """ Delete newsletter from Store """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users can only delete newsletter.')
        return redirect(reverse('home'))

    newsletter = get_object_or_404(Newsletters, pk=newsletter_id)
    if request.method == "POST":
        newsletter.delete()
        messages.success(
            request, f'{newsletter.title} has been delete successfully!'
            )
        return redirect(reverse('newsletters'))

    context = {
        'newsletter': newsletter,
    }
    return render(request, "newsletter/newsletter_delete.html", context)
