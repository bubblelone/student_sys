

from login import views
from django.urls import path, re_path

urlpatterns = [
    path('login2/', views.login2),
    path('refresh_captcha/', views.refresh_captcha),
]