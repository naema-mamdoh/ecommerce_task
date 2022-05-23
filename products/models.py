from tkinter import CASCADE
from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=200)
    describtion=models.TextField()

    def __str__(self):
        return self.name
class product(models.Model): 
    name=models.CharField(max_length=200)
    describtion=models.TextField()
    image=models.ImageField()
    price=models.DecimalField(max_digits=11,decimal_places=2)
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class card(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class cart(models.Model):
    productid =models.DecimalField(max_digits=7,decimal_places=0)
    numOfItes =models.DecimalField(max_digits=7,decimal_places=0)