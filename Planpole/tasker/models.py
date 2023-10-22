from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Высокий'),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # устанавливается автоматически при создании новой записи
    updated_at = models.DateTimeField(auto_now=True)  # автоматически обновляется при каждом сохранении записи

class FavoriteTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
