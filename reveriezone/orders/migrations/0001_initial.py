# Generated by Django 3.2.25 on 2024-04-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(1, 'ORDER_CONFIRMED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Ordereditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_cart', to='products.product')),
            ],
        ),
    ]