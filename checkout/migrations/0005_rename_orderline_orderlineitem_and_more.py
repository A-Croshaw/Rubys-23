# Generated by Django 4.2.8 on 2024-02-19 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_category'),
        ('checkout', '0004_order_original_cart_order_stripe_pid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderLine',
            new_name='OrderLineItem',
        ),
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='itemline_total',
            new_name='lineitem_total',
        ),
    ]