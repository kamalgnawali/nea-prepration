# quiz/urls.py
from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # सबै Category (क्विजका प्रकार) हरूको सूची देखाउने
    path('', views.quiz_list_view, name='quiz_list'),

    # खास Category का प्रश्नहरू देखाउने
    path('<slug:category_slug>/', views.quiz_by_category_view, name='quiz_by_category'),
]