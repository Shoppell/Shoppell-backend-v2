from django.db import models
from shop.models import Shop, Product
from user_auth.models import User

class ReportShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shop.name +" "+ self.user.mobile + " "+ self.title

class ReportProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product.name +" "+ self.user.mobile+ " "+ self.title

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title +" "+ self.user.mobile

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.ip_address

class DailyProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    view = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product.name

class DailyShopView(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    view = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.shop.name
