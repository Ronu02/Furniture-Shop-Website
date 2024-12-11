from django.db import models

class CategoryDb(models.Model):
    Category_name = models.CharField(max_length=100, null=True, blank=True)
    Category_description = models.TextField(max_length=300, null=True, blank=True)
    Category_image = models.ImageField(upload_to="Category_Images", null=True, blank=True)

class ProductDb(models.Model):
    Product_category = models.CharField(max_length=100, null=True, blank=True)
    Product_name = models.CharField(max_length=100, null=True,blank=True)
    Product_quantity = models.IntegerField(null=True, blank=True)
    Product_price = models.IntegerField(null=True, blank=True)
    Product_description = models.TextField(max_length=300, null=True, blank=True)
    Product_origin = models.CharField(max_length=100, null=True, blank=True)
    Product_manufactures = models.CharField(max_length=100, null=True, blank=True)
    Product_image1 = models.ImageField(upload_to="ProductImages", null=True, blank=True)
    Product_image2 = models.ImageField(upload_to="ProductImages", null=True, blank=True)
    Product_image3 = models.ImageField(upload_to="ProductImages", null=True, blank=True)
