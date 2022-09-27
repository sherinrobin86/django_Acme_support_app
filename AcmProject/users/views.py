from django.shortcuts import render,redirect
from .forms import NewUserForm
from users.models import Profile

# Create your views here.

def register(request):
    if request.method=='POST': 
      form=NewUserForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/users/login")
    
    form= NewUserForm(request.POST)  
        
    context={
        'form':form,
     }
    return render(request,'users/register.html',context)

def create_user(request):
  if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        dept=request.POST.get('department')
        role=request.POST.get('role')   
        pro=Profile(name=name,email=email,password=password,department=dept,role=role)
        pro.save()
        return redirect('/departments/details')
  return render(request,'users/createprofile.html')

