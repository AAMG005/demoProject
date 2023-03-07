from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("name : M.S.Dhoni\nage :42\nNationality:India\nODI_Highest_Score:183 ")

def home(request):
    return render(request, 'addition.html')

def addition(request):
    a = request.GET["num1"]
    b = request.GET["num2"]
    print(a, b)
    c = int(a) + int(b)
    print(c)
    return HttpResponse(c)
