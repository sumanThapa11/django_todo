from tasks.models import Task
from django import forms
from django.forms import ModelForm, widgets

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task....'}))

    class Meta:
        model = Task
        fields = '__all__'
        #widgets = {'complete': forms.CheckboxInput}