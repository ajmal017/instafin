# Generated by Django 2.2.2 on 2019-06-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BSEStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SecurityCode', models.IntegerField()),
                ('Symbol', models.CharField(max_length=20)),
                ('CompanyName', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=20)),
                ('Group', models.CharField(max_length=5)),
                ('FaceValue', models.IntegerField()),
                ('IsinNumber', models.CharField(max_length=100)),
                ('Industry', models.CharField(max_length=200)),
                ('Instrument', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NSEStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=20)),
                ('CompanyName', models.CharField(max_length=100)),
                ('Series', models.CharField(max_length=200)),
                ('DateOfListing', models.CharField(max_length=200)),
                ('PaidUpValue', models.IntegerField()),
                ('MarketLot', models.IntegerField()),
                ('IsinNumber', models.CharField(max_length=100)),
                ('FaceValue', models.IntegerField()),
            ],
        ),
    ]
