# Generated by Django 5.1 on 2024-09-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ratings',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
