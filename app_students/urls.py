from django.urls import path
from . import views

urlpatterns = [
    path('ce01/', views.ce01s, name='ce01s'),
    path('ce02/', views.ce02s, name='ce02s'),
    path('ce03/', views.ce03s, name='ce03s'),
    path('ce04/', views.ce04s, name='ce04s'),
]
