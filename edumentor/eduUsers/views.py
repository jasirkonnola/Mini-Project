from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from edubase.models import Question  # adjust path if needed



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
    user_questions = Question.objects.filter(user=request.user).distinct().order_by('-created_at')
    return render(request, 'eduUsers/profile.html', {
        'user_questions': user_questions,
    })



@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'eduUsers/profile_update.html', context)
