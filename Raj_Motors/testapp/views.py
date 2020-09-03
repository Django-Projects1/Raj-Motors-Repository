from django.shortcuts import render
from django.http import HttpResponseRedirect
from testapp.models import Motors,Comments,Genuine_parts,Genuine_parts_related,Other_relate_parts
from testapp.forms import signup_form,comments_form,EMI_calculate_form
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def list_view(request):
    motors_data=Motors.objects.all()
    paginator=Paginator(motors_data,3)
    page_no=request.GET.get('page')
    try:
        motors_data=paginator.page(page_no)
    except PageNotAnInteger:
        motors_data=paginator.page(1)
    except EmptyPage:
        motors_data=paginator.page(paginator.num_pages)
    return render(request,'testapp/post_list2.html',{'motors_data':motors_data})

def logout_view(request):
    return render(request,'testapp/logout.html')
def signup_view(request):
    form=signup_form()
    if request.method=='POST':
        form=signup_form(request.POST)

        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request,'testapp/signup.html',{'form':form})
def detail_view(request,id):
    motors_data=Motors.objects.get(id=id)
    comments_all=motors_data.comments.all()
    Key_feature_all=motors_data.key_fearure.all()
    Standard_feature_all=motors_data.standard_feature.all()
    c_commit=False
    if request.method=='POST':
        form=comments_form(request.POST)

        if form.is_valid():
            newcomment=form.save(commit=False)
            newcomment.post=motors_data
            newcomment.save()
            c_commit=True
    else:
        form=comments_form()
    return render(request,'testapp/post_detail.html',{'motors':motors_data,'form':form,'comments_all':comments_all,'c_commit':c_commit})


def specifications_view(request,id):
    motors_data=Motors.objects.get(id=id)
    Engine_all=motors_data.engine.all()
    Dimension_weight_all=motors_data.dimention_weight.all()
    Chasis_suspension_all=motors_data.chasis_suspension.all()
    Transmission_all=motors_data.transmission.all()
    Wheel_tyres_all=motors_data.wheel_tyre.all()
    Electricals_all=motors_data.electricals.all()
    return render(request,'testapp/specifications.html',{'motors':motors_data,'Engine_all':Engine_all,'Dimension_weight_all':Dimension_weight_all,
    'Electricals_all':Electricals_all,'Chasis_suspension_all':Chasis_suspension_all,'Transmission_all':Transmission_all,'Wheel_tyres_all':Wheel_tyres_all})

def features_view(request,id):
    motors_data=Motors.objects.get(id=id)
    Key_feature_all=motors_data.key_fearure.all()
    Standard_feature_all=motors_data.standard_feature.all()
    return render(request,'testapp/features.html',{'motors':motors_data,'Key_feature_all':Key_feature_all,
                           'Standard_feature_all':Standard_feature_all})

def variants_view(request,id):
    motors_data=Motors.objects.get(id=id)
    variants=motors_data.Variants.all()
    return render(request,'testapp/variants.html',{'variants':variants,'motors':motors_data})



def calculate_emi_view(request,id):
    motors_data=Motors.objects.get(id=id)
    form=EMI_calculate_form()
    Emi=None
    if request.method=='POST':
        form=EMI_calculate_form(request.POST)
        if form.is_valid():
            Emi_data=form.cleaned_data
            Total_Amount=Emi_data['Total_Amount']
            Down_Payment=Emi_data['Down_Payment']
            Rate_Of_Interest=Emi_data['Rate_Of_Interest']
            Tenure_In_Month=Emi_data['Tenure_In_Month']
            principal=Total_Amount-Down_Payment
            rate_month=Rate_Of_Interest/12
            rate_month=rate_month/100
            rate=((1+rate_month)**Tenure_In_Month)-1
            Emi=principal*rate_month*((1+rate_month)**Tenure_In_Month)
            Emi=Emi/rate
            Total_emi=Emi*Tenure_In_Month
            Total_interest=Total_emi-principal
            return render(request,'testapp/emi.html',{'motors':motors_data,'Total_interest':Total_interest,'Emi':Emi,'Total_payment':Total_emi})
    return render(request,'testapp/emi.html',{'form':form,'Emi':Emi})

def genuine_view(request):
    parts=Genuine_parts.objects.all()
    return render(request,'testapp/Genuine_parts.html',{'parts':parts})

def genuine_relate_view(request,id):
     parts=Genuine_parts.objects.get(id=id)
     parts_data=parts.related_parts.all()
     return render(request,'testapp/parts.html',{'parts_data':parts_data})

def other_relate_parts_view(request,id):
    parts=Genuine_parts_related.objects.get(id=id)
    others=parts.other_relate_parts.all()
    return render(request,'testapp/other_relate.html',{'others':others})

def genuine_relate_info_view(request,id):
    parts=Other_relate_parts.objects.get(id=id)
    infos=parts.relate_info.all()
    return render(request,'testapp/parts_info.html',{'infos':infos})


def Hel_floor_parts_info_view(request,id):
    parts=Genuine_parts_related.objects.get(id=id)
    infos=parts.hel_floor.all()
    return render(request,'testapp/hel_floor.html',{'infos':infos})

def contact_view(request):
    return render(request,'testapp/contact.html')

def founder_view(request):
    return render(request,'testapp/founder.html')

from testapp.forms import send_mail_form
from django.core.mail import send_mail
def send_mail_view(request):
    form=send_mail_form()
    sent=False
    fm=None
    if request.method=='POST':
        form=send_mail_form(request.POST)
        if form.is_valid():
            sent=True
            fm=form.cleaned_data
            send_mail('Bike_Booking Informations','Name='+fm['Name'] +'  Bike Name='+fm['Bike_Name'] + '  Color='+fm['Color'] ,'Raj_Motors@gmail.com',[fm['Send_To']])

    return render(request,'testapp/send_mail.html',{'form':form,'sent':sent,'fm':fm})
