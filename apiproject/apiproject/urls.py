
from django.contrib import admin
from django.urls import path,include
from startup.apiproject.task1.views import *
from rest_framework.authtoken import views 
from startup.apiproject.task1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task1/seller/',SellerViewSet.as_view(), name='seller'),
    path('task1/buyer/',BuyerViewSet.as_view(), name='buyer'),
    path('task1/login/', views.login, name='login'),
    path('task1/register/',RegistrationList.as_view(), name='register'),
    path('task1/cart/',CartItemViews.as_view(), name='product'),
    path('task1/department/',views.departmentApi),
    path('task1/login1/',loginView.as_view(),name='login1')

    

   

]
