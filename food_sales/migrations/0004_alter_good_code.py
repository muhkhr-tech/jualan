# Generated by Django 5.0.4 on 2024-05-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_sales', '0003_rename_amount_good_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]