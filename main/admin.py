from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Sellers,Prices


admin.site.site_header ='annapurna'
admin.site.site_title='Annapurna dashboard'
admin.site.index_title ='Welcome to Annapurna'


admin.site.register(Sellers)
admin.site.register(Prices)



