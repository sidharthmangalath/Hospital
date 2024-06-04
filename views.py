from django.shortcuts import render
from.models import *
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=medi()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.save()
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        obj=medi()
        obj.user=username
        obj.pwd=password
        obj.save()
    return render(request,'login.html')   
def appointment(request):
    if request.method=='POST':
        pname=request.POST['pname']
        mob=request.POST['mob']
        mail=request.POST['mail']
        date=request.POST['date']
        dept=request.POST['dept']
        doctor=request.POST['doctor']
        addr=request.POST['addr']
        obj=medi()
        obj.pname=pname
        obj.pmob=mob
        obj.pmail=mail
        obj.pdate=date
        obj.pdpt=dept
        obj.pdtr=doctor
        obj.paddr=addr
        obj.save()
    return render(request,'appointment.html')
def home(request):
        return render(request,'home.html')
def about(request):
        return render(request,'about.html')
def doctors(request):
        pro=doct1.objects.all()
        return render(request,'doctors.html',{'pro':pro})
def department(request):
        pro=dept.objects.all()
        return render(request,'department.html',{'pro':pro})

def contact(request):
        return render(request,'contact.html')

def payment(request):
        return render(request,'payment.html')


