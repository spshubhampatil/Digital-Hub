from django.shortcuts import render,redirect
from shop.models import Product,  Payment,Order
from django.contrib.auth.models import User

# Create your views here.
def downloadfree(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
        session_user=request.session.get('user')
        user=User(id=session_user.get('id'))
        if product.discount==100 and user:
            return redirect(product.file.url)
            
        else:
            return redirect('index')    
    except:
        return redirect('index')


def downloadpaidproduct(request, product_id):
    product=Product.objects.get(id=product_id)
    session_user=request.session.get('user')
    user=User(id=session_user.get('id'))
    payment=Payment.objects.filter(user=user,product=product)
    order=Order.objects.filter(user=user,product=product)
    
    if order:
        file=product.file
        if file:
            return redirect(product.file.url)
        else:
            return redirect(product.link)
    else:        
        if(len(payment)>0):
            file=product.file
            if file:
                return redirect(product.file.url)

            else:
                return redirect(product.link)
        else:
            return redirect('index')

    
        
