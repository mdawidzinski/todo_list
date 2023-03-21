from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()  # musi być, żeby jakiś model był przypisany
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegister, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

