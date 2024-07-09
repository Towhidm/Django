from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contract

# Create your views here.
def deshboard(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')
def blog(request):
    return render(request,'blog.html')
def contract(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']
        values = Contract(name=name,email=email,description=description)
        values.save()
    return render(request,'contract.html')
def about(request):
    return render(request,'about.html')