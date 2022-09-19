from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('home/', views.home, name='home'),
    path('all_signups', views.all_signups, name='all_signups'),
]