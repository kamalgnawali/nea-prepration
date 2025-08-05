# syllabus/urls.py
from django.urls import path
from . import views

app_name = 'syllabus' # यो app_name महत्त्वपूर्ण छ

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'), # /syllabus/
    path('<slug:faculty_slug>/', views.syllabus_detail, name='syllabus_detail'), # /syllabus/civil-engineering/
]