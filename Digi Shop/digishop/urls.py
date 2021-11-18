"""digishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from digishop.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT


admin.site.site_header="Digital-Hub Administration"
admin.site.site_title="Digital-Hub Admin Panel"
admin.site.index_title="Welcome to Digital-Hub Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL, document_root=STATIC_ROOT)
