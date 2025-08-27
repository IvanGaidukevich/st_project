from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=20, min_length=3, required=True, label="Логин")
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(label='Email', required=True)
    first_name = forms.CharField(max_length=20, min_length=3, required=True, label="Имя")
    last_name = forms.CharField(max_length=20, min_length=3, required=True, label="Фамилия")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user




