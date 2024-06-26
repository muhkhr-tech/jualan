# Generated by Django 5.0.4 on 2024-04-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=10)),
                ('amount', models.IntegerField(default=0)),
                ('price', models.BigIntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=10)),
                ('amount', models.IntegerField(default=0)),
                ('price', models.BigIntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
