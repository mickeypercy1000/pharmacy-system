# Generated by Django 4.1 on 2022-11-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0002_alter_drugclass_created_by_alter_drugclass_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="maximum_quantity",
            field=models.IntegerField(
                blank=True, default=None, max_length=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="reorder_quantity",
            field=models.IntegerField(
                blank=True, default=None, max_length=20, null=True
            ),
        ),
    ]
