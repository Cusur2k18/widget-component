from django.contrib import admin

from .models import Event, Measurement

admin.site.register(Event)
admin.site.register(Measurement)

# Register your models here.
