from django.contrib import admin
from .models import Student
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

admin.site.register(Student, StudentAdmin)
