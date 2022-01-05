from task1.models import SellerProfile, ClientProfile ,CartItem ,Departments
from rest_framework import serializers, status
# from models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    # def __str__(self):
    #     return self.user


class ClientSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = ClientProfile
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        buyer, created = ClientProfile.objects.update_or_create(
            user=user,
            # mobileNo=validated_data.pop('mobileNo'),
            # location=validated_data.pop('location'),
            # address=validated_data.pop('address'),

        )
        return buyer


class SellerSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = SellerProfile
        fields = ('user', 'mobileNo', 'product',
                  'product_price', 'address', 'quantity', 'shop_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        seller, created = SellerProfile.objects.update_or_create(user=user,
                                                                 mobileNo=validated_data.pop(
                                                                     'mobileNo'),
                                                                 product=validated_data.pop(
                                                                     'product'),
                                                                 product_price=validated_data.pop(
                                                                     'product_price'),
                                                                 address=validated_data.pop(
                                                                     'address'),
                                                                 quantity=validated_data.pop(
                                                                     'quantity'),
                                                                 
                                                                 shop_name=validated_data.pop(
                                                                     'shop_name'),
                                                                 )
        return seller

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')
