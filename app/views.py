from django.http import request
from django.shortcuts import render
from app.models import akm


# Create your views here.
def index(request):
    return render(request,'index.html')
def explore(request):
    return render(request,'explore.html')

def signup(request):
    return render(request,'signup.html')




def palakkad(request):
    return render(request,'palakkad.html')
def thrissur(request):
    return render(request,'thrissur.html')
def wayanad(request):
    return render(request,'wayanad.html')
def kasargod(request):
    return render(request,'kasargod.html')
def malappuram(request):
    return render(request,'malappuram.html')
def Thiruvananthapuram(request):
    return render(request,'Thiruvananthapuram.html')
def kannur(request):
    return render(request,'kannur.html')
def calicut(request):
    return render(request,'calicut.html')
def Ernakulam(request):
    return render(request,'Ernakulam.html')
def kollam(request):
    return render(request,'kollam.html')
def idduki(request):
    return render(request,'idduki.html')
def pathanamthitta(request):
    return render(request,'pathanamthitta.html')
def alapuzha(request):
    return render(request,'alapuzha.html')
def kottayam(request):
    return render(request,'kottayam.html')
def register(request):
    return render(request,'register.html')

#backend strt hear

# Create your views here.

def save(request):
    member = akm(name=request.POST['name'], email=request.POST['email'], phonenumber=request.POST['phonenumber'], password=request.POST['password'], confirmpassword=request.POST['confirmpassword'])
    member.save()
    return render(request,'signin.html')
def signin(request):
    if request.method=='POST':
        if akm.objects.filter(email=request.POST['email1'], password=request.POST['password1']).exists():
            members= akm.objects.get(email=request.POST['email1'], password=request.POST['password1'])
            return render(request, 'index.html',{'member':members})
        else:
            return render(request,'signin.html')

    else:
         return render(request,'signin.html')