from django.contrib import admin

from .models import Event, Measurement


class EventAdmin(admin.ModelAdmin):
    # Form view
    fields = ['is_active', 'name', 'level']

    # Index view
    list_display = ('_name', '_is_active', '_level', '_updated_at')


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Measurement)
