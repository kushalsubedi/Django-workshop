from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import Create_person,Update_person
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
            return redirect('index')
    context = {
        'form':form,
     }
    
    return render(request,'Home/create_person.html',context   )

def update_person (request,id):
    person = Person.objects.get(id=id)
    form = Update_person(instance=person)
    if request.method == 'POST':
        form = Update_person(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form,
     }
    return render(request,'Home/create_person.html',context )


def delete_person (request,id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('index')



    