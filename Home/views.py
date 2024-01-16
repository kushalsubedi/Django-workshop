from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import Create_person
# Create your views here.

def index(request):
    persons = Person.objects.all()

    '''
    select * from Person
    -------------------
    ram 15 Student
    samrid  55 Developer

    '''
    context = {
        'persons':persons,
     }
    return render(request,'Home/index.html',context)

def  index2 (request,id):

    person = Person.objects.get(id=id) # orm

    context = {
        'person':person,
     }
    return render(request,'Home/index2.html',context   )


def create_person (request):
    form = Create_person()
    if request.method == 'POST':
        form = Create_person(request.POST)
        print (form.data)
        if form.is_valid():
            print (form.data)
            form.save()
            return HttpResponse('Person Created')
    context = {
        'form':form,
     }
    

    
    return render(request,'Home/create_person.html',context   )
    