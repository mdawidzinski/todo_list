from django.urls import path
from .views import TodoList, CreateTask, UpdateTask, DeleteTask, Login, Register
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
   PasswordResetCompleteView

urlpatterns = [
   path('register/', Register.as_view(template_name='main/register.html'), name='Register'), # TODO convert name to lowercase
   path('login/', Login.as_view(), name='Login'),
   path('logout/', LogoutView.as_view(next_page='Login'), name='Logout'),
   path('', TodoList.as_view(), name='Todo'),
   path('create/', CreateTask.as_view(), name='Create'),
   path('update/<int:pk>/', UpdateTask.as_view(), name='Update'),
   path('delete/<int:pk>/', DeleteTask.as_view(), name='Delete'),
   path('password-reset/', PasswordResetView.as_view(template_name='main/password_reset.html'),
        name='password_reset'),  # names should match default names, or PasswordResetConfirmView.as_view(success_url=reverse_lazy('my_custom_reset_complete'))
   path('password-reset/done/', PasswordResetDoneView.as_view(template_name='main/reset_done.html'),
        name='password_reset_done'),
   path('password-reset/change/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='main/password_change.html'),
        name='password_reset_confirm'),
   path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='main/reset_complete.html'),
        name='password_reset_complete'),

]
