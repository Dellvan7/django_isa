from django.db import models
import datetime
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_creation_date = models.DateTimeField()
    items_sold = models.IntegerField()
    reputation_score = models.IntegerField()


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_creation_date = models.DateTimeField()
    wishlist = models.ForeignKey(Item)


class Item(models.Model):
    title = models.CharField()
    ISBN = models.CharField()
    author = models.CharField()
    version = models.CharField()
    description = models.CharField()


class Listing(models.Model):
    item = models.OneToOneField(Item, primary__key=True)
    date = models.DateTimeField(default=datetime.now, blank=False)
    seller = models.OneToOneField(Seller)


class Order(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=False)
    buyer = models.ForeignKey(Buyer)
    seller = models.ForeignKey(Seller)
    item = models.ForeignKey(Item)

