# Generated by Django 2.1.5 on 2020-07-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20200708_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motors',
            name='Engine_cc',
            field=models.CharField(max_length=30),
        ),
    ]
