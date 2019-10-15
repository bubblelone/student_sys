

from login import views
from django.urls import path, re_path, include

urlpatterns = [
    path('', views.login2),
]