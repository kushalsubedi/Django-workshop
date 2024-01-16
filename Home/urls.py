
from django.urls import path 

from .views import index , index2,create_person
urlpatterns = [ 
    path('a/', index, name='index'), 
    path ('b/<int:id>',index2,name="info"),
    path('create/',create_person,name="create")
]
#http://127.0.0.1:8000/