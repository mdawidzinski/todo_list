from django.urls import path
from .views import TodoList, CreateTask, UpdateTask, DeleteTask, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('register/', Register.as_view(), name='Register'), # TODO convert name to lowercase
   path('login/', Login.as_view(), name='Login'),
   path('logout/', LogoutView.as_view(next_page='Login'), name='Logout'),
   path('', TodoList.as_view(), name='Todo'),
   path('create/', CreateTask.as_view(), name='Create'),
   path('update/<int:pk>/', UpdateTask.as_view(), name='Update'),
   path('delete/<int:pk>/', DeleteTask.as_view(), name='Delete'),
]
