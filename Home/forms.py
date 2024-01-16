
from django import forms 

from .models import Person

class Create_person (forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name','age','job']


class Update_person (forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name','age','job']