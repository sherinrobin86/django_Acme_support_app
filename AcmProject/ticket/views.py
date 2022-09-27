from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from .models import Ticket

def tkt_details(request):
    tkt=Ticket.objects.all()
    context={
        'tkt':tkt
    }
    return render(request,'ticket/tkt_details.html',context) 


   
def tkt_add(request):
    if request.method=='POST':
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        priority=request.POST.get('priority')
        email=request.POST.get('email')
        phone=request.POST.get("phone")
        tkt=Ticket(subject=subject,desc=desc,priority=priority,email=email,phone=phone)
        tkt.save()
        return redirect('/ticket/tktdetails')
    return render(request,'ticket/add_tkt.html')    