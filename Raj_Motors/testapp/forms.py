from django import forms
from django.contrib.auth.models import User
from testapp.models import Comments
class signup_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class comments_form(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['name','email','comments']

class send_mail_form(forms.Form):
    Name=forms.CharField()
    Bike_Name=forms.CharField()
    Color=forms.CharField()
    Email=forms.EmailField()
    Send_To=forms.EmailField()

class EMI_calculate_form(forms.Form):
    Total_Amount=forms.IntegerField()
    Down_Payment=forms.IntegerField()
    Tenure_In_Month=forms.IntegerField()
    Rate_Of_Interest=forms.IntegerField()
