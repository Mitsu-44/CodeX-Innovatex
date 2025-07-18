from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sellers/',views.seller_list,name='sellers'),
    path('prices/',views.prices_list,name='prices'),
    path('login/',views.login_page,name='login'),
    
]
