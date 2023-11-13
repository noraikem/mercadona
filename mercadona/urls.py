"""
URL configuration for mercadona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, catalog, promotion_view
from accounts.views import logout_admin, login_admin

from mercadona import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', login_admin, name='login'),
    path('logout/', logout_admin, name='logout'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('catalog', catalog, name='catalog'),
    path('product/<str:slug>/appliquer-promotion/', promotion_view, name='promotion_view'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
