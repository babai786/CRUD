from django.shortcuts import render
from  pratikapp.forms import StudentForm
from pratikapp.models import Student
from django.http import HttpResponseRedirect

def retrive_view(request):
    list_stu=Student.objects.all().order_by('-sno')
    return render(request,'pratikapp/retrive.html',{'list_stu':list_stu})

def create_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'pratikapp/create.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect('/')

def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'pratikapp/update.html',{'student':student})
