from django.db import models
from shop.models import Product,User

class Order(models.Model):       
    user=models.ForeignKey(User, null= False, on_delete=models.CASCADE)   
    product=models.ForeignKey(Product, null= False, on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=200,null=False)
    payment_id=models.CharField(max_length=200, unique=True)
    complete=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    