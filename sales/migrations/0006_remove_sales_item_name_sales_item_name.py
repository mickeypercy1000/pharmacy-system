# Generated by Django 4.0.4 on 2022-11-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_stock_expiry_date'),
        ('sales', '0005_remove_sales_item_name_sales_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='item_name',
        ),
        migrations.AddField(
            model_name='sales',
            name='item_name',
            field=models.ManyToManyField(to='stocks.stock'),
        ),
    ]
