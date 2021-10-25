from django.shortcuts import render, HttpResponse, redirect
from shop.models import Product,ProductImage, User
from shop.utils.email_sender import sendemail
import random
import math
from django.contrib.auth.hashers import make_password, check_password


def sendotp(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    otp= math.floor(random.random()*1000000)

    html=f'''
        <h4>Hello {name},</h4>
        </br>
        <p>Your verification code is <b>{otp}</b></p>
        </br>
        <p>if you didnt requested it, you can ignore this email..</p>
        Thank You...
     '''
        
    
    if name and email:
        response=sendemail(name=name,email=email, htmlcontent=html, subject="Verify Email")

        #Email Sending...
        try:
            if(['messageId']):
                request.session['verification-code']=otp
                return HttpResponse("{'message':'success'}",status=200)
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)
            

def verifyotp(request):
    code=request.POST.get('code')    
    otp= request.session.get('verification-code')   
    
    if(str(otp)==code):                
        return HttpResponse("{'message':'success'}",status=200)
    else:
        return HttpResponse(status=400)
        
