from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from shop.models import User
from django.shortcuts import render, redirect, HttpResponse
from shop.utils.email_sender import sendemail
import math
import random


class ChangePassword(View):
    def get(self, request):
        return render(request,'changepassword.html')

    def post(self,request):
        opassword=request.POST.get('opassword')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        error=None

        session_user=request.session.get('user')
        user=User.objects.get(id=session_user.get('id'))

        flag=check_password(password=opassword, encoded=user.password)
        if flag:
            if len(password)<6:
                error='Password must be 6 charactors long!!!'
            elif len(repassword)<6:
                error='Password must be 6 charactors long!!!'
            elif password != repassword:
                error='Password must be same!!!'

            if error:
                return render(request,'changepassword.html',{'user':user ,'error':error})

            else:
                hashedpassword=make_password(password=password)
                user.password=hashedpassword
                user.save()
                return render(request,'profile.html',{'message':'Password Changed Sucessfully...', 'user':user})
    
        else:
            return render(request,'changepassword.html',{'error':'Incorrect Password...', 'user':user})