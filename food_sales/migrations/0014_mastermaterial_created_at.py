# Generated by Django 5.0.4 on 2024-05-04 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_sales', '0013_mastermaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastermaterial',
            name='created_at',
            field=models.DateField(default=None),
        ),
    ]
