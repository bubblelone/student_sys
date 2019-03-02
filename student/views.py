from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm , QueryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    students = Student.objects.all().order_by('-created_time')
    formQuery = QueryForm()


    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return redirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
            'students': students,
            'form': form,
        'formQuery': formQuery
        }
    return render(request, 'index.html', context=context)

def search_name(request):


    formQuery = QueryForm(request.POST)

    form = StudentForm()

    if formQuery.is_valid():
        cleaned_data = formQuery.cleaned_data
        search_name = cleaned_data['name']
        search_profession = cleaned_data['profession']
        search_email = cleaned_data['email']
        search_sex = cleaned_data['sex']
        search_qq = cleaned_data['qq']
        search_phone = cleaned_data['phone']


        if search_sex == None or search_sex == '':
            students = Student.objects.filter(name__contains=search_name,
                                              profession__contains=search_profession,

                                              qq__contains=search_qq,
                                              phone__contains=search_phone,
                                              email__contains=search_email,
                                              ).order_by('-created_time')
        else:
            students = Student.objects.filter(name__contains=search_name, sex=search_sex,
                                              profession__contains=search_profession,

                                              qq__contains=search_qq,
                                              phone__contains=search_phone,
                                              email__contains=search_email,
                                              ).order_by('-created_time')

    context = {
            'students': students,
            'form': form,
            'formQuery': formQuery
        }
    return render(request, 'index.html', context=context)

def hello(request):
    return render(request, 'hello.html')

def hello2(request):
    return render(request, 'hello2.html')






