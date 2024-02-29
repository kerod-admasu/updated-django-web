"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# file: projectName/ursl.py

from django.contrib import admin
from django.urls import path
from book.views  import home, about, contact_us, books,detail
from django.conf import settings
from django.conf.urls.static import static #import static setting you just added


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/',contact_us),
    path('books/', books),
    path('detail/<int:id>/', detail,name='detail'),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add the part after plus sign (+)
