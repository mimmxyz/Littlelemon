# Generated by Django 4.2.7 on 2023-11-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_menutable_inventory_alter_bookingtable_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutable',
            name='inventory',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menutable',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
