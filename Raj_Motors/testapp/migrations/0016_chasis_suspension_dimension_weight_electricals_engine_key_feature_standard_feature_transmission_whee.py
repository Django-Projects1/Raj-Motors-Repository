# Generated by Django 2.1.5 on 2020-07-10 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_auto_20200708_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chasis_suspension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chasis_type', models.CharField(max_length=50)),
                ('Front_suspension', models.CharField(max_length=50)),
                ('Rear_suspension', models.CharField(max_length=100)),
                ('bike3', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chasis_suspension', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Dimension_weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kerb_weight', models.CharField(max_length=20)),
                ('lenght', models.CharField(max_length=20)),
                ('width', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('wheelbase', models.CharField(max_length=20)),
                ('Ground_clearance', models.CharField(max_length=20)),
                ('Seat_height', models.CharField(max_length=20)),
                ('bike2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dimention_weight', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Electricals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Battery', models.CharField(max_length=50)),
                ('Headlight', models.CharField(max_length=100)),
                ('Tail_light', models.CharField(max_length=50)),
                ('bike6', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='electricals', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Engine_cc', models.CharField(max_length=50)),
                ('No_of_cylinder', models.IntegerField()),
                ('Max_Power', models.CharField(max_length=50)),
                ('max_torque', models.CharField(max_length=50)),
                ('valves_per_cylinder', models.IntegerField()),
                ('fuel_Delivery', models.CharField(max_length=50)),
                ('Cooling_system', models.CharField(max_length=50)),
                ('Starting_mechanism', models.CharField(max_length=50)),
                ('bike1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='engine', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Key_feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mf_battery', models.CharField(max_length=10)),
                ('Broader_rear_grip', models.CharField(max_length=10)),
                ('Aerodynamic_styling', models.CharField(max_length=10)),
                ('Reflector_headlight', models.CharField(max_length=10)),
                ('AHO_headlight', models.CharField(max_length=10)),
                ('bike7', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='key_fearure', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Standard_feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Speedometer', models.CharField(max_length=10)),
                ('Tachometer', models.CharField(max_length=10)),
                ('Gear_indicator', models.CharField(max_length=10)),
                ('Fuel_warning_indicator', models.CharField(max_length=10)),
                ('Fuel_gauge', models.CharField(max_length=10)),
                ('Low_oil_indicator', models.CharField(max_length=10)),
                ('Low_battery_indicator', models.CharField(max_length=10)),
                ('Pillion_seat', models.CharField(max_length=10)),
                ('Pillion_grabrail', models.CharField(max_length=10)),
                ('Engine_kill_switch', models.CharField(max_length=10)),
                ('Clock', models.CharField(max_length=10)),
                ('Tripmeter_type', models.CharField(max_length=10)),
                ('Tripmeter_count', models.CharField(max_length=10)),
                ('Pass_light', models.CharField(max_length=10)),
                ('bike8', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='standard_feature', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_of_gear', models.CharField(max_length=10)),
                ('Clutch', models.CharField(max_length=30)),
                ('bike4', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transmission', to='testapp.Motors')),
            ],
        ),
        migrations.CreateModel(
            name='Wheel_tyres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Wheel_size', models.CharField(max_length=50)),
                ('Wheel_type', models.CharField(max_length=50)),
                ('Front_tyre', models.CharField(max_length=50)),
                ('Rear_tyre', models.CharField(max_length=50)),
                ('bike5', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wheel_tyre', to='testapp.Motors')),
            ],
        ),
    ]
