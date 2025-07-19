from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sellers/',views.seller_list,name='sellers'),
    path('prices/',views.prices_list,name='prices'),
    path('register/',views.register_page,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('contact/<int:seller_id>/',views.contact_seller,name='contact'),
    path('successfull/',views.successfull,name='success'),
    path('markets/',views.market_list,name='market'),
    path('aboutus/',views.about_us,name='about'),
]
