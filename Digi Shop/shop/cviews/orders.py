from django.shortcuts import render,redirect
from shop.models import Product,Payment,User,Order
from django.db.models import Q

# Create your views here.
def my_orders(request):    
    user_id=request.session.get('user').get('id')
    user=User(id=user_id)
    session_user=request.session.get('user')    
    user=User.objects.get(id=session_user.get('id'))
    orders=Order.objects.filter(user=user,complete=True)     
        
    payment=Payment.objects.filter( ~Q(status="Failed"),user=user)      
    totalorders= list(payment)+ list(orders)     
    
    return render(request,'orders.html',{'orders':totalorders})
