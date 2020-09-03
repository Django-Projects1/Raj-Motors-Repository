# Generated by Django 2.1.5 on 2020-07-13 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0027_auto_20200713_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike_cover',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bike_cover', to='testapp.seat_cover'),
            preserve_default=False,
        ),
    ]