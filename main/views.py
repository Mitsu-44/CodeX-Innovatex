from django.shortcuts import render
from .models import Sellers,Prices
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SellerSignUpForm
from django.contrib.auth.decorators import login_required


def seller_list(request):
    sellers=Sellers.objects.all()
    return render(request,'main/seller_list.html',{'sellers':sellers})


def prices_list(request):
    prices=Prices.objects.all()
    return render(request,'main/prices_list.html',{'prices':prices})


def register_page(request):
    form = SellerSignUpForm(request.POST)
    if form.is_valid():
            user = form.save()
            Sellers.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                district=form.cleaned_data['district'],
                interested_crops=form.cleaned_data['interested_crops']
            )
            login(request, user)
            return redirect('dashboard')  # or home page
    else:
            form = SellerSignUpForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def dashboard_view(request):
    # pass more seller-related data here later
    return render(request, 'main/dashboard.html')


def home(request):
    return render(request,'main/home.html')

