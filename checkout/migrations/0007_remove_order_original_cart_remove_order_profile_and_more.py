# Generated by Django 4.2.8 on 2024-02-26 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
    ]