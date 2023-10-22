from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, FavoriteTask
from .forms import TaskForm
from django.views.generic.list import ListView
from django.shortcuts import redirect, get_object_or_404, render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        order = self.request.GET.get('order_by', 'due_date')  # По умолчанию сортируем по 'due_date'
        # Если пользователь аутентифицирован, возвращаем его задачи
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user).order_by(order)
        # Если пользователь не аутентифицирован, возвращаем пустой список задач
        else:
            return Task.objects.none()

    def get(self, request, *args, **kwargs):
        # Если пользователь не аутентифицирован, перенаправляем на пустую страницу или другую страницу на ваш выбор
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('empty_page'))
        return super().get(request, *args, **kwargs)

class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()  # Получить объект задачи, который редактируется
        context['task'] = task  # Передать объект задачи в контекст шаблона
        return context

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()  # Получить объект задачи, который удаляется
        context['task'] = task  # Передать объект задачи в контекст шаблона
        return context

def toggle_favorite(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    user = request.user

    favorite, created = FavoriteTask.objects.get_or_create(task=task, user=user)

    if not created:  # Если задача уже в избранном, удаляем её
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    return JsonResponse({'status': 'added'})

class FavoriteTaskListView(ListView):
    model = Task
    template_name = 'favorite_task_list.html'

    def get_queryset(self):
        return Task.objects.filter(favoritetask__user=self.request.user)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def empty_page(request):
    return render(request, 'empty_page.html')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.request.user == self.object.user
        return context

def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.user == task.user:  # убедитесь, что текущий пользователь владелец этой задачи
        task.is_completed = not task.is_completed
        task.save()
    return redirect('name_of_your_task_list_view')
