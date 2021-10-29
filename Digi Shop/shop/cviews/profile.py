from django.shortcuts import render,redirect
# from shop.models import User
from django.contrib.auth.models import User


def profile(request):    
    session_user=request.session.get('user')     
    user=User.objects.get(id=session_user.get('id'))    
    data={'user':user}
    return render(request,'profile.html',data)