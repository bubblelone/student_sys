from django.contrib import admin
from .models import Student, Student2, grade
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','profession','email','qq','phone','status','created_time')
    list_filter = ('name', 'profession')
    fieldsets = (
        (None, {
            'fields':
                ('name',
                 ('sex', 'profession'),
                 ('email', 'qq', 'phone'),
                 'status',)
        }),
    )

class Student2Admin(admin.ModelAdmin):
    list_display = ('id','name','age')

class gradeAdmin(admin.ModelAdmin):
    list_display = ('id','no','kemu','score')


admin.site.register(Student, StudentAdmin)
admin.site.register(Student2, Student2Admin)
admin.site.register(grade, gradeAdmin)
