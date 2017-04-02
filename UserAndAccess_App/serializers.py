from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups','password')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    productImage = serializers.ImageField(max_length=None,use_url=True)

    class Meta:
        model = Product
        fields = ('productid','productqty',productImage','productname', 'productprice', 'productdesc')

#added for image start

#class ImageSerializer(serializers.ModelSerializer)
     #image = serializers.ImageField(max_length=None,use_url=True)
     	#class Meta:
        #model = Product
        #fields = ('productid','productImage','productname', 'productprice', 'productdesc')

#added for image end