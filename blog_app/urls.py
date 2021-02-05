"""blog_app URL Configuration

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
from django.urls import path
from blog_app_sample import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.user_login, name="user_login"),
    path('user_registration' , views.user_registration, name="user_registration"),
    path('user_view' , views.user_view, name="user_view"),
    path('user_logout' , views.user_logout, name="user_logout"),


#admin views


    path('admin_login' , views.admin_login, name="admin_login"),
    path('admin_view' , views.admin_view, name="admin_view"),
    path('admin_view_save' , views.admin_view_save, name="admin_view_save"),
    path('admin_logout' , views.admin_logout, name="admin_logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

