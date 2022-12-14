# Generated by Django 4.0.4 on 2023-01-03 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0003_customer_address_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='businessType',
        ),
        migrations.AddField(
            model_name='customer',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
