from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)    
    description=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    discount=models.IntegerField(default=0)
    file=models.FileField(upload_to='uploads/files', null=True, blank=True)
    thumbnail=models.ImageField(upload_to='uploads/thumbnails')
    link=models.CharField(null=True,blank=True, max_length=200)
    filesize=models.CharField(null=True, max_length=15)

    @staticmethod
    def get_all_products_by_Categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads/images', blank=True)