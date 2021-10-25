from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from shop.models import User
from django.shortcuts import render, redirect

class LoginView(View):
    return_url=None
    def get(self, request):
        LoginView.return_url=request.GET.get('return_url')
        return render(request,'login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
            # active=User.objects.get(active=active)
            if user.active ==True:

                flag=check_password(password=password, encoded=user.password)
                if(flag):
                    temp={}
                    temp['email']=user.email
                    temp['id']=user.id
                    request.session['user']=temp
                    if LoginView.return_url:
                        return redirect(LoginView.return_url)
                    return redirect('index')
                else:
                    return render(request,'login.html',{'error':"Invalide Credentials!!!"})
            else:
                return render(request,'login.html',{'error':"Your account has been blocked, Please contact admin!!!"})
        except:
            return render(request,'login.html',{'error':"Invalide Credentials!!!"})
