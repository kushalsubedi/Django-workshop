from django import forms
from django.contrib.auth.models import User 


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(max_length=32)
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']