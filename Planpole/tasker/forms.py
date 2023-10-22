from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название задачи'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'placeholder': 'Введите описание задачи'
    }))

    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, initial=2, widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    due_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
