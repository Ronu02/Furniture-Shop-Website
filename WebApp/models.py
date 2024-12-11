from django.db import models

class ContactDb(models.Model):
    First_name = models.CharField(max_length=100, null=True, blank=True)
    Last_name = models.CharField(max_length=100, null=True, blank=True)
    Email_address = models.EmailField(max_length=200, null=True, blank=True)
    Message = models.TextField(max_length=300, null=True, blank=True)

class SignupDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Repeat_password = models.CharField(max_length=50, null=True, blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)

class OrderDb(models.Model):
    Country = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=300, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)

