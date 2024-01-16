from django.contrib import admin

from .models import Person
# Register your models here.

admin.site.register(Person) #this will add the Person model to the admin page 