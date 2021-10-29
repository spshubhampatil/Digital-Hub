from django.shortcuts import render,redirect
# from shop.models import User
from django.views import View
from django.contrib.auth.models import User

class updateprofile(View):
    def get(self,request):
        session_user=request.session.get('user')    
        user=User.objects.get(id=session_user.get('id'))    
        data={'user':user}
        return render(request,'updateprofile.html',data)

    def post(self,request):
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        # phone=request.POST.get('phone')
        print(fname)
        print(lname)
        error=None
        if fname:
            if len(fname)<2:
                error='Please enter valid name..'

        if lname:
            if len(lname)<2:
                error='Please enter valid name..'

        # if phone:
        #     if len(phone)<6:
        #         error='Phone must be 10 charactors long'        

        if error:
            return render(request,'updateprofile.html',{'error':error})
        else:
            session_user=request.session.get('user')    
            user=User.objects.get(id=session_user.get('id'))   
            if fname:
                user.first_name=fname

            if lname:
                user.last_name=lname

            # if phone:
            #     user.phone=phone
                
            user.save()           
            return render(request,'profile.html',{'message':'Profile Updated Sucessfully...', 'user':user})


