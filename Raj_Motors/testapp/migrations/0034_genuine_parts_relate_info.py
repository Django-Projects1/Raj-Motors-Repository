# Generated by Django 2.1.5 on 2020-07-14 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0033_auto_20200714_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='genuine_parts_relate_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50)),
                ('Applicable', models.TextField()),
                ('sp1', models.CharField(blank=True, max_length=50)),
                ('sp2', models.CharField(blank=True, max_length=50)),
                ('sp3', models.CharField(blank=True, max_length=50)),
                ('sp4', models.CharField(blank=True, max_length=50)),
                ('sp5', models.CharField(blank=True, max_length=50)),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='relate_info', to='testapp.Other_relate_parts')),
            ],
        ),
    ]
