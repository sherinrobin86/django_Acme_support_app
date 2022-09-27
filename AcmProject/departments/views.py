# from django.contrib.auth.decorators import login_required
from .models import Department
from multiprocessing import context
from django.shortcuts import  render, redirect
from django.http import HttpResponse

def sample(request):
    return HttpResponse("hi")


# Create your views here.
def details(request):
    dept=Department.objects.all()
    context={
        'dept':dept
    }

    return render(request,'departments/index.html',context) 

def dept_det(request,id):
     dept=Department.objects.get(id=id)
     context={
          'dept':dept
    }  
     return render(request,'departments/departmentdet.html',context)  

   
def add_dept(request):
    if request.method=='POST':
        name=request.POST.get('name')
        
        desc=request.POST.get('desc') 
       
        dept=Department(name=name,description=desc)
        dept.save()
        return redirect('/departments/details')
    return render(request,'departments/add_dept.html')


def update_dept(request,id):
    dept=Department.objects.get(id=id)
    if request.method=='POST':
        dept.name=request.POST.get('name')
        dept.description=request.POST.get('desc') 
        dept.save()
        return redirect('/departments/details')
    context={
         'dept':dept
              }  
    return render(request,'departments/updatedept.html',context)     


def delete_dept(request,id):
    dept=Department.objects.get(id=id)   
    context={
         'dept':dept
              }  
    if request.method=='POST':   
        dept.delete()
    
        return redirect('/departments/details')
    return render(request,'departments/del_dept.html',context) 
 

