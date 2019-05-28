from django.urls import path

from . import views

urlpatterns = [
    path('current_event/', views.index, name='index'),
]