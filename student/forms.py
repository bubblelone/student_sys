"""
@Version: 1.0
@Project: PythonCookBook
@Author: bubblelone
@Date: 2019/2/25 14:38
@File: forms.py
@License: MIT
"""
from django import forms
from .models import Student
from django.utils.translation import gettext_lazy

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

        return int(cleaned_data)

    class Meta:
        model = Student
        fields =  (
        'name','sex','profession',
        'email', 'qq', 'phone'
    )

class QueryForm(forms.ModelForm):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),

    ]
    name = forms.CharField(required=False, label='姓名')

    profession = forms.CharField(required=False, label='职业')
    email = forms.CharField(required=False, label='email')
    qq = forms.CharField(required=False, label='qq')
    phone = forms.CharField(required=False, label='电话')
    class Meta:
        model = Student
        fields = ('name','sex', 'profession', 'qq', 'phone')

