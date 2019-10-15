"""student_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.urls import include
from student import views
from login import views as l_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    path('search_name/', views.search_name),
    path('hello/', views.hello),
    path('hello2/', views.hello2),
    path('upload/', views.excel_upload),
    path('upload2/', views.excel_upload2),
    path('csrf/', views.get_csrf),
    path('login/PostLogin', l_views.login1),
    re_path(r'^accounts/login$', views.index),
    #path('login/', l_views.login2),
    path('login/', include('login.urls')),
    path('logout/', l_views.logout1),
    path('hello3/', views.hello3),
    path('login3/', views.login3),
    path('list1/', views.list1),
    path('list2/', views.list2),
    path('hello4/', views.hello4),
    path('index/', l_views.index),
    path('register/', l_views.register),
    path('login2/', l_views.login4),
    path('captcha/', include('captcha.urls')),
    path('refresh_captcha/', l_views.refresh_captcha),


]
