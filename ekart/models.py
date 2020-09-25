from django.db import models

# Create your models here.

# Create your models here.
from django.contrib.auth.models import AbstractUser




class Category(models.Model):
    cname = models.CharField(max_length=30)
    cname_desc = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    # class Meta:
    #     ordering = ['-cname,']

    def __str__(self):
        return self.cname    

class Products(models.Model):
    product_cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    product_description = models.CharField(max_length=200)
    product_price = models.FloatField(max_length=100)
    product_image = models.ImageField(upload_to='media/images')


    def __str__(self):
        return self.product_name


