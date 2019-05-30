from django.urls import path

from . import views

urlpatterns = [
	path('agent/', views.index, name="index")
]
