# Generated by Django 2.1.5 on 2020-07-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_motors_engine_cc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motors',
            name='Engine_cc',
            field=models.IntegerField(default=0),
        ),
    ]
