# Generated by Django 2.1.5 on 2020-07-10 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0016_chasis_suspension_dimension_weight_electricals_engine_key_feature_standard_feature_transmission_whee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dimension_weight',
            old_name='lenght',
            new_name='length',
        ),
    ]