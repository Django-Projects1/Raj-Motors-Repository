# Generated by Django 2.1.5 on 2020-07-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0024_auto_20200713_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='bike_seat_cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bike', models.CharField(max_length=10)),
                ('bike_img', models.ImageField(null=True, upload_to='', verbose_name='upload_to=pictures/')),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='variants',
            name='var1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='variants',
            name='var2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='variants',
            name='var3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='variants',
            name='var4',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='variants',
            name='var5',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
