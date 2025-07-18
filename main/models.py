from django.db import models


class Sellers(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=150)
    contact=models.CharField(max_length=20)
    experience=models.CharField(max_length=10)
    interested=models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Prices(models.Model):
    vegie_name=models.CharField(max_length=30)
    min_price=models.IntegerField(default=0)
    max_price=models.IntegerField(default=0)
    last_updated=models.DateField(auto_now=True)
    
    @property
    def avg(self):
        return ((self.min_price + self.max_price) // 2)
    
    def __str__ (self):
        return self.vegie_name


