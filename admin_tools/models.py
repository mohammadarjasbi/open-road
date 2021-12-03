from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DecimalField


class Product_type(models.Model):
    name = models.CharField(max_length=125, null=False)

    def __str__(self):
        return self.name


class Business(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.ForeignKey(Product_type, null=False,
                             on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='businesses')
    Price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.Product_Name
