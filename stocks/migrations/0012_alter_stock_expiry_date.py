# Generated by Django 4.0.4 on 2022-11-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0011_alter_stock_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
