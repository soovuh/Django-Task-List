from django import forms

from .models import Task

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'name', 'description'}


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'name', 'description', 'is_complete'}

