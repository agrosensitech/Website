from django.shortcuts import render, HttpResponse

def home(request):
    print("Hello")
    return HttpResponse(request,"Hello this is tanmay")
