#Model class in models module defines all the common behaviours or characteristics that are needed by models in as in
# application in django. eg. to store,read ,delete models from database.
#Thus inheriting this product class from Model class, we won't have to take care for above functions, we've inherited them
#attributes of a product that we need to know??
#name,price,image_url

from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    image_url = models.CharField(max_length = 2083)


class Offer(models.Model):
    code = models.CharField(max_length = 20)
    description = models.TextField()
    discount = models.FloatField()
