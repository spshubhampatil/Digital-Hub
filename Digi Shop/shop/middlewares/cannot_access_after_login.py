from django.shortcuts import render, redirect



def cantaccessafterlogin(get_response):

    def middleware(request):
        user=request.session.get('user')
        if user:
            return redirect('index')
              
        else:
            return get_response(request)
            
       
    return middleware