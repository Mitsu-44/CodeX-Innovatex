from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sellers

class SellerSignUpForm(UserCreationForm):
    contact = forms.CharField(max_length=20)
    location = forms.CharField(max_length=100)
    experience = forms.CharField(max_length=100)
    interested = forms.CharField(
    widget=forms.Textarea(attrs={
        'rows': 2,
        'placeholder': 'e.g. Tomatoes, Onions, Wheat'
    })
)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'contact', 'location', 'experience', 'interested']



class SellerDashboardForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = ['contact', 'location', 'experience', 'interested']
        widgets = {
            'interested': forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. Tomatoes, Onions, Wheat'}),
        }

