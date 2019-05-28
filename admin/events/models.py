from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.TextField()
    is_active = models.BooleanField(default=False)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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