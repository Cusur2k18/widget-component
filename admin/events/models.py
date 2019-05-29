from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.TextField()
    is_active = models.BooleanField(default=False)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _name(self):
        return self.name
    _name.short_description = 'Nombre'

    def _is_active(self):
        return self.is_active
    _is_active.short_description = 'Activo'
    _is_active.boolean = True

    def _level(self):
        return self.level
    _level.short_description = 'Nivel'

    def _created_at(self):
        return self.created_at
    _created_at.short_description = 'Fecha creación'

    def _updated_at(self):
        return self.updated_at
    _updated_at.short_description = 'Ultima actualización'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.TextField()
    value = models.TextField()
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name