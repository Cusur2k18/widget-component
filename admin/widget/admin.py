from django.contrib import admin

from .models import Agent, Metric


class AgentAdmin(admin.ModelAdmin):
    admin.site.site_url
    # Form view
    fields = ['is_active', 'name', 'level']

    # Index view
    list_display = ('_name', '_is_active', '_level', '_updated_at')


# Register your models here.
admin.site.register(Agent, AgentAdmin)
admin.site.register(Metric)
