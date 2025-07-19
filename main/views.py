from django.shortcuts import render,redirect
from .models import Sellers,Prices,ContactMessage
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SellerSignUpForm,SellerDashboardForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def seller_list(request):
    sellers=Sellers.objects.all()
    return render(request,'main/seller_list.html',{'sellers':sellers})


def prices_list(request):
    prices=Prices.objects.all()
    return render(request,'main/prices_list.html',{'prices':prices})


def register_page(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Sellers.objects.create(
               user=user,
                contact=form.cleaned_data['contact'],
                location=form.cleaned_data['location'],
                experience=form.cleaned_data['experience'],
                interested=form.cleaned_data['interested']
            )
            login(request, user)
            return redirect('dashboard')  
    else:
            form = SellerSignUpForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def dashboard_view(request):
    seller = Sellers.objects.get(user=request.user)
  
    if request.method == 'POST':
        form = SellerDashboardForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # redirect to dashboard after save
    else:
        form = SellerDashboardForm(instance=seller)

    # Later you can add messages here, e.g. messages = Message.objects.filter(seller=seller)
        messages = seller.messages.all().order_by('-timestamp')
    context = {
        'form': form,
        'messages': messages,
    }
    return render(request, 'main/dashboard.html', context)




def contact_seller(request, seller_id):
    seller = get_object_or_404(Sellers, id=seller_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            seller=seller,
            sender_name=name,
            sender_phone=phone,
            message=message
        )
        return redirect('dashboard')  # or redirect to dashboard if logged in
    return render(request, 'main/contact.html', {'seller': seller})




def contact_us(request,seller_id):
    return render(request,'main/contact.html')

def successfull(request):
    return render(request,'main/success.html')

def market_list(request):
    return render(request,'main/markets.html')

def about_us(request):
    return render(request,'main/aboutus.html')
def home(request):
    return render(request,'main/home.html')

