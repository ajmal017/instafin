# Generated by Django 2.2.2 on 2019-06-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thematic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalIndia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricVehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EvergreenStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HalalStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IncredibleIndia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SmartCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SociallyResponsible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]
