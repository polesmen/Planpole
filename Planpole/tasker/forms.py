from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(label='Название задачи', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название задачи'
    }))

    description = forms.CharField(label='Описание задачи', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'placeholder': 'Введите описание задачи'
    }))

    priority = forms.ChoiceField(label='Приоритет', choices=Task.PRIORITY_CHOICES, initial=2, widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    due_date = forms.DateField(label='Срок',widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
