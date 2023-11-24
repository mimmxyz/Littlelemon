# Generated by Django 4.2.7 on 2023-11-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTable',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('noofguests', models.IntegerField(max_length=6)),
                ('bookingdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuTable',
            fields=[
                ('id', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField(max_length=5)),
            ],
        ),
    ]
