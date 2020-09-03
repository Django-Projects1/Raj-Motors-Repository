from django.db import models

# Create your models here.
class Motors(models.Model):
    V_model=models.CharField(max_length=20)
    slug=models.SlugField(max_length=20)
    variant=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pictures/',null=True)
    body=models.TextField(null=True,blank=True)
    Ex_showroom_price=models.FloatField()
    Engine_cc=models.CharField(max_length=10,null=True)
    Mileage=models.CharField(max_length=10,null=True)
    Max_Power=models.CharField(max_length=30,null=True)
    Ignition=models.CharField(max_length=80,null=True)
    insurance_Tp=models.CharField(max_length=30)
    RTO=models.FloatField()
    Gl=models.FloatField()
    Acc_hel=models.FloatField()
    on_road=models.FloatField()

class Comments(models.Model):
    post=models.ForeignKey(Motors,related_name='comments',on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    comments=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

class Engine(models.Model):
    bike1=models.ForeignKey(Motors,related_name='engine',on_delete=models.DO_NOTHING)
    Engine_cc=models.CharField(max_length=50)
    No_of_cylinder=models.IntegerField()
    Max_Power=models.CharField(max_length=50)
    max_torque=models.CharField(max_length=50)
    valves_per_cylinder=models.IntegerField()
    fuel_Delivery=models.CharField(max_length=60)
    Cooling_system=models.CharField(max_length=50)
    Starting_mechanism=models.CharField(max_length=50)

class Dimension_weight(models.Model):
    bike2=models.ForeignKey(Motors,related_name='dimention_weight',on_delete=models.DO_NOTHING)
    kerb_weight=models.CharField(max_length=20)
    length=models.CharField(max_length=20)
    width=models.CharField(max_length=20)
    height=models.CharField(max_length=20)
    wheelbase=models.CharField(max_length=20)
    Ground_clearance=models.CharField(max_length=20)
    Seat_height=models.CharField(max_length=20)

class Chasis_suspension(models.Model):
    bike3=models.ForeignKey(Motors,related_name='chasis_suspension',on_delete=models.DO_NOTHING)
    Chasis_type=models.CharField(max_length=50)
    Front_suspension=models.CharField(max_length=60)
    Rear_suspension=models.CharField(max_length=100)

class Transmission(models.Model):
     bike4=models.ForeignKey(Motors,related_name='transmission',on_delete=models.DO_NOTHING)
     No_of_gear=models.CharField(max_length=10)
     Clutch=models.CharField(max_length=50)

class Wheel_tyres(models.Model):
     bike5=models.ForeignKey(Motors,related_name='wheel_tyre',on_delete=models.DO_NOTHING)
     Wheel_size=models.CharField(max_length=50)
     Wheel_type=models.CharField(max_length=50)
     Front_tyre=models.CharField(max_length=50)
     Rear_tyre=models.CharField(max_length=50)

class Electricals(models.Model):
     bike6=models.ForeignKey(Motors,related_name='electricals',on_delete=models.DO_NOTHING)
     Battery=models.CharField(max_length=50)
     Headlight=models.CharField(max_length=100)
     Tail_light=models.CharField(max_length=50)

class Key_feature(models.Model):
    bike7=models.ForeignKey(Motors,related_name='key_fearure',on_delete=models.DO_NOTHING)
    Mf_battery=models.CharField(max_length=10)
    Broader_rear_grip=models.CharField(max_length=10)
    Aerodynamic_styling=models.CharField(max_length=10)
    Reflector_headlight=models.CharField(max_length=10)
    AHO_headlight=models.CharField(max_length=10)

class Standard_feature(models.Model):
    bike8=models.ForeignKey(Motors,related_name='standard_feature',on_delete=models.DO_NOTHING)
    Speedometer=models.CharField(max_length=10)
    Tachometer=models.CharField(max_length=10)
    Gear_indicator=models.CharField(max_length=10)
    Fuel_warning_indicator=models.CharField(max_length=10)
    Fuel_gauge=models.CharField(max_length=10)
    Low_oil_indicator=models.CharField(max_length=10)
    Low_battery_indicator=models.CharField(max_length=10)
    Pillion_seat=models.CharField(max_length=10)
    Pillion_grabrail=models.CharField(max_length=10)
    Engine_kill_switch=models.CharField(max_length=10)
    Clock=models.CharField(max_length=10)
    Tripmeter_type=models.CharField(max_length=10)
    Tripmeter_count=models.CharField(max_length=10)
    Pass_light=models.CharField(max_length=10)


class variants(models.Model):
    bike=models.ForeignKey(Motors,related_name='Variants',on_delete=models.DO_NOTHING)
    var1=models.CharField(max_length=500,blank=True)
    var2=models.CharField(max_length=500,blank=True)
    var3=models.CharField(max_length=500,blank=True)
    var4=models.CharField(max_length=500,blank=True)
    var5=models.CharField(max_length=500,blank=True)

class Genuine_parts(models.Model):
    name=models.CharField(max_length=20)
    bike_img=models.ImageField(upload_to='pictures/')
    body=models.TextField(null=True,blank=True)

class Genuine_parts_related(models.Model):
    parts=models.ForeignKey(Genuine_parts,related_name='related_parts',on_delete=models.DO_NOTHING)
    parts_img=models.ImageField(upload_to='pictures/')
    parts_name=models.CharField(max_length=20)
    parts_body=models.TextField(blank=True)

class Other_relate_parts(models.Model):
    parts=models.ForeignKey(Genuine_parts_related,related_name='other_relate_parts',on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pictures/')

class genuine_parts_relate_info(models.Model):
    parts=models.ForeignKey(Other_relate_parts,related_name='relate_info',on_delete=models.DO_NOTHING)
    Description=models.CharField(max_length=50)
    Applicable=models.TextField()
    MRP=models.CharField(max_length=20)
    sp1=models.CharField(max_length=50,blank=True)
    sp2=models.CharField(max_length=50,blank=True)
    sp3=models.CharField(max_length=50,blank=True)
    sp4=models.CharField(max_length=50,blank=True)
    sp5=models.CharField(max_length=50,blank=True)

class Hel_floor_parts_info(models.Model):
    parts=models.ForeignKey(Genuine_parts_related,related_name='hel_floor',on_delete=models.DO_NOTHING)
    Description=models.CharField(max_length=50)
    Applicable=models.TextField()
    MRP=models.CharField(max_length=20)
    sp1=models.CharField(max_length=50,blank=True)
    sp2=models.CharField(max_length=50,blank=True)
    sp3=models.CharField(max_length=50,blank=True)
    sp4=models.CharField(max_length=50,blank=True)
    sp5=models.CharField(max_length=50,blank=True)
