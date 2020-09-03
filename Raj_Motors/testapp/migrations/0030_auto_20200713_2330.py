# Generated by Django 2.1.5 on 2020-07-13 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0029_auto_20200713_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genuine_parts_related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_img', models.ImageField(upload_to='pictures/')),
                ('parts_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='genuine_parts',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='genuine_parts_related',
            name='parts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_parts', to='testapp.Genuine_parts'),
        ),
    ]