# Generated by Django 4.0.4 on 2022-11-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0016_alter_stock_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugclass',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]