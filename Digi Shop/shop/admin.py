from django.contrib import admin
from shop.models import Product, ProductImage, Payment,Contact,Order
from shop.models.coupon import Coupon
from shop.models.product import Category
from django.utils.html import format_html
from digishop.settings import PAYMENT_API_KEY,PAYMENT_API_AUTH_TOKEN
import math
from django.contrib.auth.models import User
from instamojo_wrapper import Instamojo
API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

# Register your models here.
class ProductImageModel(admin.StackedInline):
    model=ProductImage

class OrderbasketModel(admin.StackedInline):
    model=Order


class ProductModel(admin.ModelAdmin):
    list_display=['id','name','get_category','get_description','get_price','get_discount','get_sale_price','file','get_thumbnail']
    inlines=[ProductImageModel]   

    def get_thumbnail(self,obj):
        return format_html(f'''
        <img height="50px" src='{obj.thumbnail.url}'/>
        ''')

    def get_sale_price(self,obj):
        return ' ₹ ' + str((obj.price)-(obj.price * (obj.discount/100)))

    def get_description(self, obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:15]}...</span>')

    def get_price(self,obj):
        return ' ₹ ' +  str(obj.price)

    def get_discount(self,obj):
        return str(obj.discount) + ' % '

    def get_category(self,obj):
        return str(obj.category)

    get_sale_price.short_description='Sale Price'
    get_description.short_description='Description'
    get_price.short_description='Price'
    get_discount.short_description='Discount'
    get_category.short_description='Category'
    get_thumbnail.short_description='Icon'




class PaymentModel(admin.ModelAdmin):
    list_display=['id','get_user','get_product','get_status','amount']    

    def get_status(self,obj):
        # response = API.payment_request_payment_status(obj.payment_request_id, obj.payment_id)
        # obj.paymentDetails=response
        if obj.status != "Failed":
            return True
        else:
            return False

    def get_user(self,obj):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{obj.user.id}">{obj.user}</a>')
    
    def get_product(self,obj):
        return format_html(f'<a target="_blank" href="/admin/shop/product/{obj.product.id}">{obj.product}</a>')
    
    get_user.short_description='User'
    get_product.short_description='Product'
    get_status.short_description='Status'
    get_status.boolean=True
    

class ContactModel(admin.ModelAdmin):
    list_display=['sno','name','phone','email','get_content','timeStamp']

    def get_content(self, obj):
        return format_html(f'<span title="{obj.content}">{obj.content[0:50]}...</span>')

    get_content.short_description='Message'

# class OrderModel(admin.ModelAdmin):
#     list_display=['id','user','product','payment_method','complete']
#     sortable_by=['id','user']
#     list_editable=['complete']

admin.site.register(Product, ProductModel)
admin.site.register(Payment,PaymentModel)
admin.site.register(Contact,ContactModel)
admin.site.register(Category)
# admin.site.register(Coupon)
# admin.site.register(Order,OrderModel)
