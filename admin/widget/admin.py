from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Agent, Metric

class BaseAdmin(AdminSite):
	site_header = 'Administracion del Widget Cusur'


class CustomUserAdmin(UserAdmin):
	pass


class AgentAdmin(admin.ModelAdmin):
    admin.site.site_url
    # Form view
    fields = ['is_active', 'name', 'level']

    # Index view
    list_display = ('_name', '_is_active', '_level', '_updated_at')


# Register your models here.
admin_site = BaseAdmin(name="base")
admin_site.register(User, CustomUserAdmin)
admin_site.register(Agent, AgentAdmin)
admin_site.register(Metric)
