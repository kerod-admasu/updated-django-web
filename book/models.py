# file: appName/models.py

from django.db import models

# Create your models here.

# company info 
# products 

      
class Product(models.Model):
   book=models.CharField(max_length=100,null=True)
   author= models.CharField(max_length=100,null=True)
   product_description = models.TextField()   
   category = models.CharField(max_length=100,null=True)
   image  = models.ImageField(null=True)
   price   = models.FloatField(null=True)
   date   = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self) -> str:
      return self.author
   

class ContactInfo(models.Model):
   name  = models.CharField(max_length=100)
   email  = models.EmailField()
   text  = models.TextField()

   def __str__(self) -> str:
      return self.name