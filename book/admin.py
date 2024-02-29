# file: appName/admin.py

from django.contrib import admin
from book.models import Product
from book.models import ContactInfo

# Register your models here.

admin.site.register(Product)
admin.site.register(ContactInfo)


