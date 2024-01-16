
from django.urls import path 

from .views import index , index2,create_person,update_person,delete_person
urlpatterns = [ 
    path('a/', index, name='index'),  #listing
    path ('b/<int:id>',index2,name="info"), #retrive
    path('create/',create_person,name="create"), #create
    path ('update/<int:id>',update_person,name="update") ,#update
    path ('delete/<int:id>',delete_person,name="delete") ,#delete

]
#http://127.0.0.1:8000/