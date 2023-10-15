from django.urls import path
from tasker import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),  # Главная страница
    path('task/create/', views.CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/update/', views.UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete_task'),
]