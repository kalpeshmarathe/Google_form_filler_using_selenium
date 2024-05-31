# myapp/urls.py
from django.urls import path
from .views import automate_and_send_email
from django.http import HttpResponse
from . import views

def home(request):
    return HttpResponse('Welcome to the home page!')

def automate_and_send_email(request):
    # Your existing code for automate_and_send_email
    pass


urlpatterns = [
    path('', views.home, name='home'),
    path('automate-and-send-email/', views.automate_and_send_email, name='automate_and_send_email'),
]
