# Generated by Django 4.0.4 on 2022-11-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_alter_stock_item_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'active'), ('Inactive', 'inactive')], default=None, max_length=20, null=True),
        ),
    ]