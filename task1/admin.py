from django.contrib import admin
from .models import SellerProfile,ClientProfile,CartItem
# Register your models here.
admin.site.register(SellerProfile)
admin.site.register(ClientProfile)
admin.site.register(CartItem)