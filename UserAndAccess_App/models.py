from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

     
class Product(models.Model):
	productid = models.CharField(max_length=50)
	productqty = models.CharField(max_length=10	)
	productImage = models.ImageField(upload_to='Images') #added for image start ,default='Images/None/No-image.jpg'
	productname = models.CharField(max_length=20)
	productprice = models.CharField(max_length=50)
	productdesc = models.CharField(max_length=50)

	def __unicode__(self):
	     return self.productid