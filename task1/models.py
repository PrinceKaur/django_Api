from django.db import models

# Create your models here.

from django.contrib.auth.models import User


# Create your models here.


class SellerProfile(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)


    mobileNo = models.CharField(max_length=40, default=None)
    product= models.CharField(max_length=30, default=None)
    product_price = models.PositiveIntegerField(max_length=30, default=None)
    address = models.CharField(max_length=30, default=None)
    quantity= models.PositiveIntegerField(max_length=30, default=None)
    shop_name = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User, models.SET_DEFAULT, default=None)


    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)