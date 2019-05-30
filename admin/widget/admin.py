from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Agent, Metric

class BaseAdmin(AdminSite):
	site_header = 'Administracion del Widget Cusur'


class CustomUserAdmin(UserAdmin):
	pass

class MetricInline(admin.TabularInline):
    model = Metric
    extra = 1


class AgentAdmin(admin.ModelAdmin):
    admin.site.site_url

    # Index view
    list_display = ('_name', '_is_active', '_level', '_updated_at',)
    
    # form view
    fieldsets = [
        ('Información del agente', { 'fields': ['is_active', 'name', 'level',], 'classes': ['agent-info']}),
    ]

    inlines = [MetricInline]

    actions = ['toogle_active',]

    def toogle_active(modeladmin, request, queryset):
        # import pdb; pdb.set_trace()
        for e in queryset.all():
            e.is_active=True
            e.save()
    toogle_active.short_description = 'Activar agente'



# Register your models here.
admin_site = BaseAdmin(name="base")
admin_site.register(User, CustomUserAdmin)
admin_site.register(Agent, AgentAdmin)
