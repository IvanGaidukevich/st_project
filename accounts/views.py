from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")  # тут поменяем на login
    else:
        form = UserCreationForm()
        return render(request,
                      template_name='registration/registration.html',
                      context={'form': form})
