from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already registered and logged in.')
        return redirect('edubase:home')

    if request.method == "POST": 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'eduUsers/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('edubase:home')
    return render(request, 'eduUsers/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('edubase:home')


@login_required
def profile(request):
    return render(request, 'eduUsers/profile.html')
