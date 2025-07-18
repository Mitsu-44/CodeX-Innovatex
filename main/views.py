from django.shortcuts import render
from .models import Sellers,Prices

def seller_list(request):
    sellers=Sellers.objects.all()
    return render(request,'main/seller_list.html',{'sellers':sellers})


def prices_list(request):
    prices=Prices.objects.all()
    return render(request,'main/prices_list.html',{'prices':prices})


def login_page(request):
    return render(request,'main/login.html')

def home(request):
    return render(request,'main/home.html')