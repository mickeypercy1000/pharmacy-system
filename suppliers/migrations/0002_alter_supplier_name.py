# Generated by Django 4.0.4 on 2022-11-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
