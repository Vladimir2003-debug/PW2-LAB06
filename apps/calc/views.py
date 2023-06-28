from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def add(request):
    var1 = request.GET['numb1']
    var2 = request.GET['numb2']

    result = var1 + var2

    return render(request, 'result.html',{'result':result})