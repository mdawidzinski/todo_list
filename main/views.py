from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from datetime import datetime
from .models import Task


class Register(FormView):  # TODO add email
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):  # TODO redirect ?
        if self.request.user.is_authenticated:
            return redirect('Todo')
        return super(Register, self).get(*args, **kwargs)


class Login(LoginView):  # TODO password_reset, password_change
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Todo')


class TodoList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Todo_List'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Todo_List'] = context['Todo_List'].filter(user=self.request.user)
        context['count'] = context['Todo_List'].filter(complete=False).count()
        search_task = self.request.GET.get('search') or ''
        if search_task:
            context['Todo_List'] = context['Todo_List'].filter(task__icontains=search_task)

        context['search_task'] = search_task
        context['date'] = datetime.now().strftime("%B %d, %Y")
        return context


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task', 'description', 'complete']
    success_url = reverse_lazy('Todo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task', 'description', 'complete']
    success_url = reverse_lazy('Todo')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'Delete'
    success_url = reverse_lazy('Todo')

