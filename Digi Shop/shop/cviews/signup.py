from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from shop.models import User
from django.shortcuts import render, HttpResponse, redirect
from shop.utils.email_sender import sendemail

class SignupView(View):
    def get(self, request):
        return render(request,'signup.html')
        
    def post(self, request):
        thank=False
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            phone=request.POST.get('phone')
            hashedpassword=make_password(password=password)
            user= User(name=name, email=email,password=hashedpassword,phone=phone)
            user.save()
            sendEmailAfterCreateAccount(user)
            thank=True   
            return render(request,'login.html',{'thank':thank})
        except:
            return render(request,'signup.html',{'error':"User already existed..."})


def sendEmailAfterCreateAccount(user):
    html=f'''
    <p>Dear <b>{user.name}</b>,
    <p>Welcome to our family,</p>
    <p>Your Email has been verified successfully,</p>
    <p>Now, You can login with your email & password..</p>
    <p>Thank You..</p>
    '''
    sendemail(user.name,user.email,'Welcome to our family..',html)
        