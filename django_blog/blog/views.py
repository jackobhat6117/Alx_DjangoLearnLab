from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})   

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST, instance = request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = CustomUserCreationForm(instance = request.user)

    return render(request, 'blog/profile', {'u_form': u_form})