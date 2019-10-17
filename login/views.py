from django.shortcuts import render, redirect
from . import models
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login , logout, authenticate
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json


# Create your views here.

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            try:
                #user = models.User.objects.get(name=username)
                user1 = authenticate(username=username, password=password)
                #print(user1)
                if user1:
                    login(request, user1)
                else:
                    return JsonResponse({"code": 0})
            except Exception as e:
                print(e)
                return JsonResponse({"code":0})
            #if user1.password == password:
             #   return JsonResponse({"code":1})
            #else:
            return JsonResponse({"code":1})





def login2(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        ver = request.POST.get("ver")
        hashkey = request.POST.get("hashkey")


        if username.strip() == '':
            return JsonResponse(
                {"code": 1001, "msg": "用户名不能为空"}
            )
        elif password == '':
            return JsonResponse(
                {"code": 1002,
                 "msg": "密码不能为空"}
            )

        elif ver == '':
            return JsonResponse({"code":1004, "msg": "验证码不能为空"})

        elif ver and hashkey:
            if not jarge_captcha(ver, hashkey):
                return JsonResponse({"code":1005, "msg": "验证码错误"})
        if username and password:

            try:
                user = models.User.objects.get(name=username)
            except:
                return JsonResponse(
                    {"code": 1003,
                     "msg": "用户名或密码错误"}
                )
            if user.password == password:
                return JsonResponse({"code": 0, "msg": "登录成功"})
            else:
                return JsonResponse({"code": 1003, "msg": "用户名或密码错误"})

    return render(request, 'login1.html')

def logout1(request):
    logout(request)

    return redirect('/login/')

def index(request):
    return render(request, 'index1.html')

def register(request):
    return render(request, 'register.html')

def login4(request):

    return render(request, 'login.html')

def captcha():
    # 验证码，第一次请求
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha

def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            # 如果验证码匹配
            if get_captcha.response == captchaStr.lower():
                return True
        except:
            return False
    else:
        return False

# 刷新验证码
# path: /ims/refresh_captcha

def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')


