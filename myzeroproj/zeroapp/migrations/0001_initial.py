# Generated by Django 2.2.3 on 2019-07-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=35)),
                ('countrycode', models.CharField(max_length=3)),
                ('district', models.CharField(max_length=20)),
                ('population', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='', max_length=20)),
                ('lastname', models.CharField(default='', max_length=20)),
                ('gender', models.CharField(default='', max_length=10)),
                ('mobile', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
