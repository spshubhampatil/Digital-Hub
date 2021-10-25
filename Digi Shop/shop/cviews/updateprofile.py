from django.shortcuts import render,redirect
from shop.models import User
from django.views import View


class updateprofile(View):
    def get(self,request):
        session_user=request.session.get('user')    
        user=User.objects.get(id=session_user.get('id'))    
        data={'user':user}
        return render(request,'updateprofile.html',data)

    def post(self,request):
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        error=None
        if name:
            if len(name)<6:
                error='Name must be 6 charactors long'
        if phone:
            if len(phone)<6:
                error='Phone must be 10 charactors long'        

        if error:
            return render(request,'updateprofile.html',{'error':error})
        else:
            session_user=request.session.get('user')    
            user=User.objects.get(id=session_user.get('id'))   
            if name:
                user.name=name

            if phone:
                user.phone=phone
                
            user.save()           
            return render(request,'profile.html',{'message':'Profile Updated Sucessfully...', 'user':user})


