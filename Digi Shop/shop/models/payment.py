from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

payment_mode = (('None','None'),
            ('Online', 'Online'),
           ('Offline', 'Offline'),          
           )

payment_status = (('Failed','Failed'),
            ('Credit', 'Credit'),
           ('Pending', 'Pending'),          
           )


class Payment(models.Model):
    product=models.ForeignKey(Product, null= False, on_delete=models.CASCADE)   
    user=models.ForeignKey(User, null= False, on_delete=models.CASCADE)   
    payment_request_id=models.CharField(max_length=200,null=False, unique=True)
    payment_id=models.CharField(max_length=200, unique=False)
    status=models.CharField(max_length=20,choices=payment_status, default='Pending')
    payment_mode=models.CharField(max_length=20,choices=payment_mode, default='None')
    amount=models.CharField(max_length=20,null=True,blank=True,default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

