from django import forms 
from django.forms import ModelForm
from .models import Tasks, Classes

class ClassForm(ModelForm):
    class Meta:
        model = Classes
        fields = ('name', 'course_code','semester', 'grade', 'GPA','completed')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'course_code': forms.TextInput(attrs={'class':'form-control'}),
            'semester': forms.Select(attrs={'class':'form-control'}),
            'grade': forms.TextInput(attrs={'class':'form-control'}),
            'GPA': forms.TextInput(attrs={'class':'form-control'}),
        }

class TaskForm(ModelForm):
    class Meta: 
        model = Tasks
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'classes': forms.Select(attrs={'class':'form-control'}),
            'due_date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD'}),
        }