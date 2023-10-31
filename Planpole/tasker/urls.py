from django.urls import path
from tasker import views
from django.contrib.auth import views as auth_views
from .views import TaskDetailView, FavoriteTaskListView


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),  # Главная страница
    path('task/create/', views.CreateTaskView.as_view(), name='create_task'),
    path('task/<int:task_id>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('task/<int:pk>/update/', views.UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete_task'),

    path('favorite-tasks/', views.FavoriteTaskListView.as_view(), name='favorite_task_list'),
    path('login/', auth_views.LoginView.as_view(next_page='task_list'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('empty/', views.empty_page, name='empty_page'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('toggle-completion/<int:task_id>/', views.toggle_task_completion, name='toggle_completion'),
    path('favorite/', FavoriteTaskListView.as_view(), name='favorite_tasks'),
]