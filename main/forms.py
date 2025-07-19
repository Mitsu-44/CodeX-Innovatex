from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SellerSignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    district = forms.CharField(max_length=100)
    interested_crops = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone', 'district', 'interested_crops']
