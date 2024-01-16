from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserCreationForm
# Create your views here.


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print (form.data)
        if form.is_valid():
            print (form.data)
            form.save()
            return redirect('index')
        
    context = {
        'form':form,
     }
    return render(request,'Register/register.html',context)

def login_user(request):

    if request.method == 'POST':
  
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            print ("Login Succesful")
            return redirect('index')
        else :
            print ("Login Failed")
            return redirect('login')    
    

    return render(request,'Register/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')