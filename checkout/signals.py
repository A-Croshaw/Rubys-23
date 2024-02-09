from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineTotal


@receiver(post_save, sender=OrderLineTotal)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.total_update()


@receiver(post_delete, sender=OrderLineTotal)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.total_update()