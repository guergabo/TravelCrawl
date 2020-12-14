# Generated by Django 2.2.12 on 2020-12-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=250)),
                ('startdate', models.CharField(max_length=250)),
                ('enddate', models.CharField(max_length=250)),
                ('out_airlines', models.CharField(max_length=250)),
                ('in_airlines', models.CharField(max_length=250)),
                ('out_dep_times', models.CharField(max_length=250)),
                ('in_dep_times', models.CharField(max_length=250)),
                ('out_arr_times', models.CharField(max_length=250)),
                ('in_arr_times', models.CharField(max_length=250)),
                ('out_stops', models.CharField(max_length=250)),
                ('in_stops', models.CharField(max_length=250)),
                ('out_durations', models.CharField(max_length=250)),
                ('in_durations', models.CharField(max_length=250)),
                ('prices', models.CharField(max_length=250)),
                ('check_out', models.CharField(max_length=250, unique=True)),
            ],
        ),
    ]
