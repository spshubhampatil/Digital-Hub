from django.views import View
from shop.models import Contact, User
from django.shortcuts import render, redirect


class ContactView(View):    

    def get(self, request):
        return render(request,'contact.html')

    def post(self,request): 
        if request.session.get('user'):       
            user_id=request.session.get('user').get('id')
            user=User(id=user_id)
            session_user=request.session.get('user')    
            user=User.objects.get(id=session_user.get('id'))        
            if user:
                name = user.name           
                phone = request.POST.get('phone')
                email = user.email                  
                content = request.POST.get('content')

                values={'name':name,'email':email,'phone':phone,'content':content}
                contact = Contact(name=name,email=email,phone=phone,content=content)

                thank=False
                error=None            
                if len(phone) < 10:
                    error='Please, Enter valid phone!!!'
                elif len(content) < 4:
                    error='Please, Enter message!!!'
                if error:
                    return render(request,'contact.html',{'error':error,'value':values})
                else:                        
                    contact.save()
                    thank=True
                    return render(request,'contact.html',{'thank':thank})
            else:
                return render(request,'contact.html',{'error':"Please Login to contact us!!!"})
        else:
            return render(request,'contact.html',{'error':"Please Login to contact us!!!"})