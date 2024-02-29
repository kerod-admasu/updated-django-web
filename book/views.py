# file: appName/views.py

from django.shortcuts import render, HttpResponse #import HttpResponse
from .models import*
# Create your views here.


def home(request):
  
   books = Product.objects.all()
   
   data ={
      
      'books':books,
   }
   
   return render(request, 'home.html',data)

def detail(request, id):
   books = Product.objects.get(id=id)
   
   data ={
      
      'books':books,
   }

def about(request):
   return render(request,'about.html')


def contact_us(request):
      
   if request.method =='POST':
      user_name  = request.POST.get('name')
      user_email  = request.POST.get('email')
      user_text  = request.POST.get('text')
   
      obj = ContactInfo()
      
      obj.name = user_name
      obj.email =user_email
      obj.text = user_text
      obj.save()
   return render(request, 'contact.html')

def books(request):
   return render(request,'books.html')

def detail(request, id):
   book = Product.objects.get(id=id)
   
   
   data ={
      
      'book':book,
   }
   return render(request,'detail.html',data)


