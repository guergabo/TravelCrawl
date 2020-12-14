# Generated by Django 2.2.12 on 2020-12-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=250)),
                ('country_name', models.CharField(max_length=250)),
                ('iata_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
    ]
