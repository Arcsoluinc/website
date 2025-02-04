from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Company

# Create your views here.

def home(request):
    company = Company.objects.all()
    return render(request, "main/home.html", {"company": company})

def about(request):
    company = Company.objects.all()
    return render(request, "main/about.html", {"company": company})