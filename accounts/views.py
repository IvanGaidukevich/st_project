from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")  # тут поменяем на login
    else:
        form = CustomUserCreationForm()
        return render(request,
                      template_name='registration/registration.html',
                      context={'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("blog:post_list")
    else:
        form = AuthenticationForm()
    return render(request,
                  template_name='registration/login.html',
                  context={'form': form})


def logout_view(request):
    logout(request)
    return redirect("blog:post_list")
