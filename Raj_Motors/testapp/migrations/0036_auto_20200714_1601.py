# Generated by Django 2.1.5 on 2020-07-14 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0035_genuine_parts_relate_info_mrp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hel_floor_parts_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50)),
                ('Applicable', models.TextField()),
                ('MRP', models.CharField(max_length=20)),
                ('sp1', models.CharField(blank=True, max_length=50)),
                ('sp2', models.CharField(blank=True, max_length=50)),
                ('sp3', models.CharField(blank=True, max_length=50)),
                ('sp4', models.CharField(blank=True, max_length=50)),
                ('sp5', models.CharField(blank=True, max_length=50)),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hel_floor', to='testapp.Genuine_parts_related')),
            ],
        ),
        migrations.AlterField(
            model_name='genuine_parts_relate_info',
            name='MRP',
            field=models.CharField(max_length=20),
        ),
    ]
