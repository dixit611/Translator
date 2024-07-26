# translator/urls.py

from django.urls import path
from . import views  # Import views from the translator app

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('', views.home, name='home'),  # The home view
    path('translate/', views.translate, name='translate'),  # The translate view
    path('voice-command/', views.voice_command, name='voice_command'),
    path('convert-text-to-speech/', views.convert_text_to_speech, name='convert_text_to_speech'),
]

