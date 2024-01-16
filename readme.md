
# Django  

start django project 
``` bash
django-admin startproject project1 .
```
start django app
``` bash
python manage.py startapp Home
```
run server
``` bash
python manage.py runserver
```
# create a helloworld view 
``` python
# Home/views.py
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world.")
```
# add url to project1/urls.py 

``` python  
#project's url file 
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
]
```
# add url to Home/urls.py 
``` python
#app's url file
from django.urls import path
from .views import index 
urlpatterns = [
    path('',index, name='index'),
]
```