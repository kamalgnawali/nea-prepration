# notes/urls.py
from django.urls import path
from . import views

app_name = 'notes' # app_name सुनिश्चित गर्नुहोस्

urlpatterns = [
    path('', views.subject_list_view, name='subject_list'), # /notes/
    # विषय अनुसार टपिक लिस्ट गर्न र कुनै खास टपिकको नोट देखाउन
    path('<slug:subject_slug>/', views.topic_detail_view, name='topic_list_and_detail'),
    # यदि सिधै टपिकमा जानु छ भने (वैकल्पिक)
    path('<slug:subject_slug>/<slug:topic_slug>/', views.topic_detail_view, name='topic_detail'),
]