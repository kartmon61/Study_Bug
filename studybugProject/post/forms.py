from django import forms
from .models import University, Student
from .widgets import CounterTextInput, starWidget

# 생략
class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        field = ['name','department','grade']
        widgets = {
            'name':CounterTextInput,
            'department':CounterTextInput,
            'grade':CounterTextInput,
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'grade': starWidget,
        }