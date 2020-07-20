from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    gender = [
        ('1', '男'),
        ('2', '女'),
    ]
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'layui-input'}))
    password1 = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'layui-input'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'layui-input'}))
    email = forms.EmailField(label="邮箱地址", max_length=256,
                                widget=forms.EmailInput(attrs={'class': 'layui-input'}))
    sex = forms.ChoiceField(label='性别', choices=gender,)

    captcha = CaptchaField(label='验证码')


