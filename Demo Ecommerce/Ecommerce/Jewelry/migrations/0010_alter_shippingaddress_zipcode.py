# Generated by Django 4.2.11 on 2024-03-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jewelry', '0009_item_total_ordered_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=2),
        ),
    ]
