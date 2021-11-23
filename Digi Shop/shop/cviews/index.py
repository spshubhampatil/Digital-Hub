from django.shortcuts import render,redirect
from shop.models import Product,Coupon
from shop.models.product import Category
from django.core.paginator import Paginator



# Create your views here.
def index(request):    
    products=Product.objects.filter(active=True)
    Categories=Category.objects.all();   
    categoryID=request.GET.get('category')
    coupons=Coupon.objects.all()
    
    for co in coupons:
        print(list(co.product.all().values_list('name')))
    if categoryID:
        products=Product.get_all_products_by_Categoryid(categoryID);        
        
        data={'categories':Categories,'products':products}
        return render(request,'category.html', data)
    else:
        products=Product.objects.all(); 
        paginator = Paginator(products, 8)
    
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data={'categories':Categories,'page_obj': page_obj}
        return render(request,'index.html', data)

def search(request):
    query = request.GET['query']
    Categories=Category.objects.all();   
    categoryID=request.GET.get('category')
    if len(query) > 78 or len(query)<1:
        products = Product.objects.none()
    else:
        productsName = Product.objects.filter(name__icontains=query)
        productsDescription = Product.objects.filter(description__icontains=query)
        productsCategory=Category.objects.filter(name__icontains=query)
        
        if productsCategory:
            for product in productsCategory:              
            
                products=Product.objects.filter(category=product)                         
        
            data = {'products': products,'query': query,'categories':Categories}
            return render(request, 'search.html', data)

        else:
            products = productsName.union(productsDescription)             
          
    data = {'products': products, 'query': query}
    return render(request, 'search.html', data)


def logout(request):
    request.session.clear()
    return redirect('index')

def tandc(request):
    return render(request,'tandc.html')

def ppolicy(request):
    return render(request,'ppolicy.html')