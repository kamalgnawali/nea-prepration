# my_practice/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # Home page को लागि
from django.conf import settings # थप्नुहोस्
from django.conf.urls.static import static
from .views import contact_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # तपाईंको Home Page
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'), # 'about' नामको URL
    path('notes/', include('notes.urls')),
    path('quiz/', include('quiz.urls')),
    path('syllabus/', include('syllabus.urls')), # नयाँ: syllabus urls लाई समावेश गर्ने
    # अरू Apps का URL हरू यहाँ थप्न सक्नुहुन्छ
  path('contact/',include('core.urls'), name='contact'),
  path('accounts/',include('accounts.urls')),
  
  


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)