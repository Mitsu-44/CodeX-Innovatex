from django.db import models
from django.contrib.auth.models import User

class Sellers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location=models.CharField(max_length=150)
    contact=models.CharField(max_length=20)
    experience=models.CharField(max_length=10)
    interested=models.CharField(max_length=20)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Prices(models.Model):
    vegie_name=models.CharField(max_length=30)
    unit=models.CharField(max_length=10)
    price=models.IntegerField(default=0)
    last_updated=models.DateField(auto_now=True)
    def __str__ (self):
        return self.vegie_name

class ContactMessage(models.Model):
    seller = models.ForeignKey('Sellers', on_delete=models.CASCADE, related_name='messages')
    sender_name = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender_name} to {self.seller.user.username}"
    
    


