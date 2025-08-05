# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import CustomUserRegistrationForm, LoginForm
from .models import Profile
from quiz.models import QuizAttempt


def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'accounts/profile.html', {'profile': profile})
@login_required
def edit_profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        photo = request.FILES.get('photo')

        profile.bio = bio
        if photo:
            profile.profile_pic = photo
        profile.save()
        return redirect('profile')  # save गरेपछि profile page मा redirect गर्न सक्नुहुन्छ

    # GET request को लागि form display गर्ने part
    return render(request, 'accounts/edit_profile.html', {'profile': profile})




@login_required
def quiz_history(request):
    attempts = QuizAttempt.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'quiz/quiz_history.html', {'attempts': attempts})



@login_required
def dashboard(request):
    results = QuizAttempt.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'accounts/dashboard.html', {'results': results})
