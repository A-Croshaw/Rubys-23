# Generated by Django 4.2.8 on 2024-02-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_category_alter_book_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('non-fiction', 'Non-Fiction'), ('fiction', 'Fiction'), ('childrens', 'Childrens')], default='Non-Fiction', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used')], default='new', max_length=50),
        ),
    ]