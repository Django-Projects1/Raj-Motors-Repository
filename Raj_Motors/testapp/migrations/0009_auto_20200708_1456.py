# Generated by Django 2.1.5 on 2020-07-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20200708_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motors',
            name='Engine_cc',
            field=models.IntegerField(),
        ),
    ]