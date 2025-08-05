# accounts/urls.py

from django.urls import path
from .views import (
    register_view, profile_view, edit_profile_view, quiz_history,
    login_view, logout_view, dashboard
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('profile/history/', quiz_history, name='quiz_history'),
    path('dashboard/', dashboard, name='dashboard'),
]
