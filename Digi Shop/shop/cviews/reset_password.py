from django.views import View
from django.contrib.auth.hashers import make_password, check_password
# from shop.models import User
from django.shortcuts import render, redirect, HttpResponse
from shop.utils.email_sender import sendemail
import math
import random
from django.contrib.auth.models import User

class ResetPassword(View):
    
    def get(self, request):
        return render(request,'reset_password.html',{'step1':True})
       

    def post(self,request):
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        error=None
        if len(password)<6:
            error='Password must be 6 charactors long'
        elif len(repassword)<6:
            error='Password must be 6 charactors long'
        elif password != repassword:
            error='Password must be same'

        if error:
            return render(request,'reset_password.html',{'step3':True, 'error':error})
        else:
            email=request.session.get('reset-password-email')
            user=User.objects.get(email=email)
            user.password=make_password(password)
            user.save()
            # request.session.clear()
            sendEmailAfterChangePassword(user)
            return render(request,'login.html',{'message':'Password Changed Sucessfully...'})


def sendEmailAfterChangePassword(user):
    html=f'''
    <p>Dear <b>{user.email}</b>,
    <p>Your Password has been changed successfully,</p>
    <p>Now, You can login with new password..</p>
    <p>Thank You..</p>
    '''
    sendemail(user.email,user.email,'Password Changed Successfully..',html)
        


def verifyResetPasswordCode(request):
    code=request.POST.get('code')
    session_code=request.session['reset-password-verification-code']
    if code==str(session_code):
        return render(request,'reset_password.html',{'step3':True})
    else:
        return render(request,'reset_password.html',{'step2':True})


class PasswordResetVerification(View):     

    def post(self,request):
        email=request.POST.get('email')

        try:
            user=User.objects.get(email=email)
            otp=math.floor(random.random()*1000000)
            html=f'''
            <p>Your Reset Password Verification Code is <b> {otp} </b></p>
            '''
            sendemail("User",email,"Password Reset verification code", html)
            request.session['reset-password-verification-code']=otp
            request.session['reset-password-email']=email
            return render(request,'reset_password.html',{'step2':True})

        except:
            return redirect('reset-password')