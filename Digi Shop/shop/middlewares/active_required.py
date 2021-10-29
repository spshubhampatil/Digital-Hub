from django.shortcuts import render, redirect
# from shop.models import User
from django.contrib.auth.models import User


def active_required(get_response):

    def middleware(request, product_id=None):
        user=request.session.get('user')
        if user:            
            user=User.objects.get(id=user.get('id'))

            if user.is_active:
                response=None
                if product_id:
                    response=get_response(request, product_id)
                else:
                    response=get_response(request)
                return response
            else:
                url=request.path
                request.session.clear()
                return redirect(f'/login?return_url={url}')
        else:
            url=request.path
            request.session.clear()
            return redirect(f'/login?return_url={url}')

    return middleware