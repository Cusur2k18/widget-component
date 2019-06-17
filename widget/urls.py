from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('agent/', views.widget, name="index"),
	path('agent-preview/<int:id>', views.preview, name="agent_preview"),
	path('cache/', views.clear_cache, name="erase_cache"),
]
