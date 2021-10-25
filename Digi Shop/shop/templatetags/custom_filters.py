from django import template

register = template.Library()

@register.filter(name='rupee')
def addRupeeSign(value):
    return f'₹ {value}'

@register.filter(name='percent')
def addPercentSign(value):
    return f'{value} % '

@register.filter(name='saleprice')
def getsaleprice(product):
    return (product.price-(product.price*(product.discount/100)))

