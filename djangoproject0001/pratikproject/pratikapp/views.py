from django.shortcuts import render
from pratikapp.models import Employee
from . forms import EmployeeForm
from django.http import HttpResponseRedirect
# Create your views here.

def retrive_view(request):
    employees=Employee.objects.all()
    return render(request,'pratikapp/index.html',{'employees':employees})


def create_view(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect('/')
        # Create your views here.
    return render(request,'pratikapp/create.html',{'form':form})


def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return  HttpResponseRedirect('/')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect('/')
    return render(request,'pratikapp/update.html',{'employee':employee})
