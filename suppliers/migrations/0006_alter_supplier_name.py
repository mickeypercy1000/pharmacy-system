# Generated by Django 4.0.4 on 2023-01-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_alter_supplier_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
