from django.contrib import admin
from testapp.models import Motors,variants,Other_relate_parts,Hel_floor_parts_info,Genuine_parts,genuine_parts_relate_info,Genuine_parts_related,Comments,Engine,Dimension_weight,Chasis_suspension,Transmission,Wheel_tyres,Electricals,Key_feature,Standard_feature
# Register your models here.
class MotorsAdmin(admin.ModelAdmin):
    list_display=['V_model','variant','image','body','Ex_showroom_price','Engine_cc','Mileage','Max_Power','Ignition','insurance_Tp','RTO','Gl','Acc_hel','on_road']
    prepopulated_fields={'slug':('V_model',)}
    search_fields=('V_model',)
admin.site.register(Motors,MotorsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display=['name','email','comments']
    search_fields=('body','name',)
admin.site.register(Comments,CommentsAdmin)

class EngineAdmin(admin.ModelAdmin):
    list_display=['Engine_cc','No_of_cylinder','Max_Power','max_torque','valves_per_cylinder','fuel_Delivery','Cooling_system','Starting_mechanism']
admin.site.register(Engine,EngineAdmin)

class Dimension_weightAdmin(admin.ModelAdmin):
    list_display=['kerb_weight','length','width','height','wheelbase','Ground_clearance','Seat_height']
admin.site.register(Dimension_weight,Dimension_weightAdmin)

class Chasis_suspensionAdmin(admin.ModelAdmin):
    list_display=['Chasis_type','Front_suspension','Rear_suspension']
admin.site.register(Chasis_suspension,Chasis_suspensionAdmin)

class TransmissionAdmin(admin.ModelAdmin):
    list_display=['No_of_gear','Clutch']
admin.site.register(Transmission,TransmissionAdmin)

class Wheel_tyresAdmin(admin.ModelAdmin):
    list_display=['Wheel_size','Wheel_type','Front_tyre','Rear_tyre']
admin.site.register(Wheel_tyres,Wheel_tyresAdmin)


class ElectricalsAdmin(admin.ModelAdmin):
    list_display=['Battery','Headlight','Tail_light']
admin.site.register(Electricals,ElectricalsAdmin)

class Key_featureAdmin(admin.ModelAdmin):
    list_display=['Mf_battery','Broader_rear_grip','Aerodynamic_styling','Reflector_headlight','AHO_headlight']
admin.site.register(Key_feature,Key_featureAdmin)

class Standard_featureAdmin(admin.ModelAdmin):
    list_display=['Speedometer','Tachometer','Gear_indicator','Fuel_warning_indicator','Fuel_gauge','Low_oil_indicator',
    'Low_battery_indicator','Pillion_seat','Pillion_grabrail','Engine_kill_switch','Clock','Tripmeter_type','Tripmeter_count','Pass_light']
admin.site.register(Standard_feature,Standard_featureAdmin)

class variantsAdmin(admin.ModelAdmin):
    list_display=['var1','var2','var3','var4','var5']
admin.site.register(variants,variantsAdmin)

class Genuine_partsAdmin(admin.ModelAdmin):
    list_display=['name','body']
admin.site.register(Genuine_parts,Genuine_partsAdmin)

class Genuine_parts_relatedAdmin(admin.ModelAdmin):
    list_display=['parts_name']
admin.site.register(Genuine_parts_related,Genuine_parts_relatedAdmin)

class Other_relate_partsAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Other_relate_parts,Other_relate_partsAdmin)

class genuine_parts_relate_infoAdmin(admin.ModelAdmin):
    list_display=['Description','Applicable','MRP','sp1','sp2','sp3','sp4','sp5']
admin.site.register(genuine_parts_relate_info,genuine_parts_relate_infoAdmin)

class Hel_floor_parts_infoAdmin(admin.ModelAdmin):
    list_display=['Description','Applicable','MRP','sp1','sp2','sp3','sp4','sp5']
admin.site.register(Hel_floor_parts_info,Hel_floor_parts_infoAdmin)
