from django.shortcuts import render
from myapp.forms import StuForm
from .models import Student
from django.views.generic import ListView

def index(request):
        stu =StuForm(request.POST or None)
        if stu.is_valid():
           newpart=stu.save()
           print(newpart)
        context= {'form': stu }
        return render(request,'index.html',{'form':StuForm, 'Student':Student.objects.all})
