# Generated by Django 4.2.8 on 2024-02-18 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_category'),
        ('checkout', '0002_rename_original_bag_order_original_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('itemline_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
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
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='OrderLineTotal',
        ),
        migrations.AddField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order'),
        ),
    ]