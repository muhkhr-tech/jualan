# Generated by Django 5.0.4 on 2024-05-01 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_sales', '0002_good_ingredient_shopping_shoppinggood_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='amount',
            new_name='stock',
        ),
    ]