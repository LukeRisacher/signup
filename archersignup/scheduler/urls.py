from django.urls import path
from . import views

urlpatterns = [
    path('', views.regpage, name='regpage'),
    path('home/', views.home, name='home'),
    path('all_signups', views.all_signups, name='all_signups'),
]