from django.db import models

# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1,'男'),
        (2, '女'),

    ]

    STATUS_ITEMS = [
        (1, '申请'),
        (2, '通过'),
        (0, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别', blank=True)
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email', max_length=128)
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='电话')
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name='审核状态', default=1)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '学员信息'

