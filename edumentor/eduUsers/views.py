from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    if request.method == "POST": 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully created for {username}! Login In Now')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'eduUsers/register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('edubase:home')
    return render(request, 'eduUsers/login.html')

def logout(request):
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')



