# Generated by Django 4.2.11 on 2024-03-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jewelry', '0007_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
