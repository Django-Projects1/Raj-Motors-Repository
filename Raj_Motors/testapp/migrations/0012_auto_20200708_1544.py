# Generated by Django 2.1.5 on 2020-07-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_auto_20200708_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='motors',
            name='Ignition',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='motors',
            name='Max_Power',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='motors',
            name='Mileage',
            field=models.CharField(max_length=10, null=True),
        ),
    ]