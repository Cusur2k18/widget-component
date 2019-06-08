from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Agent, Metric, Widget

class BaseAdmin(AdminSite):
    site_header = 'Administracion del Widget Cusur'



class CustomUserAdmin(UserAdmin):
	pass

class MetricInline(admin.TabularInline):
    model = Metric
    extra = 1

class WidgetInline(admin.TabularInline):
    model = Widget
    extra = 1


class AgentAdmin(admin.ModelAdmin):

    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js', 'admin/js/jquery.init.js', 'js/main.js',)
        css = {
            'all': ('scss/admin.css',)
        }

    # Index view
    list_display = ('_name', '_is_active', '_updated_at',)
    
    # form view
    fieldsets = [
        ('Información del agente', { 'fields': ['is_active', 'name',], 'classes': ['agent-info']}),
    ]

    inlines = [WidgetInline, MetricInline]

    actions = ['toogle_active',]

    def toogle_active(modeladmin, request, queryset):
        # import pdb; pdb.set_trace()
        for e in queryset.all():
            e.is_active=not e.is_active
            e.save()
    toogle_active.short_description = 'Activar/Desactivar agente(s)'



# Register your models here.
admin_site = BaseAdmin(name="base")
admin_site.register(User, CustomUserAdmin)
admin_site.register(Agent, AgentAdmin)
