# Generated by Django 5.0.4 on 2024-05-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_sales', '0011_sellingfoodingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellingfood',
            name='good_name',
        ),
        migrations.RemoveField(
            model_name='sellingfood',
            name='good_price',
        ),
        migrations.RemoveField(
            model_name='sellingfood',
            name='good_price_sale',
        ),
    ]
