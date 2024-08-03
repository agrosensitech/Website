from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.templatetags.static import static
import json
# Create your views here.
from .models import Plant, Contact


def home(request):
    return render(request,'agro/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        Contact(name=name,phone_no=phone,email=email,description=desc).save()
        return render(request,"agro/contact.html",{
            "message":"Your response has been recorded"
        })
    return render(request,"agro/contact.html")

def about(request):
    return render(request,"agro/about.html")

def details(request,id):
    plant = Plant.objects.get(id=id)
    data = plant.table_data
    
    return render(request,"agro/details.html",context={
        "plant":plant,
        "message":"",
        "data":data
    })

def gallery(request):
    plants = Plant.objects.all()
    return render(request,"agro/gallery.html",context={
        "plants":plants
    })

def weather(request):
    STATIC_URL = static('')
    return render(request,"agro/weather.html",{
        'STATIC_URL':STATIC_URL
    })

def login_user(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
                username=username,
                password=password
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'Login failed!'
    return render(request,"agro/login.html",context={
        "message":message
    })

def logout_user(request):
    if request.user.is_authenticated:
        logout(request) 
    return redirect('home')

def dashboard(request):
    return render(request,"agro/dashboard.html")