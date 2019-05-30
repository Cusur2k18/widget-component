from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField('Nombre', max_length=100)
    is_active = models.BooleanField('Activo',default=False)
    level = models.IntegerField('Nivel', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'

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

    def validate_uniqueness_active(self):
        if self.is_active:
            # select the other active agent
            qs = type(self).objects.filter(is_active=True)
            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
                # and deactive them
            qs.update(is_active=False)
    
    def save(self, *args, **kwargs):
        self.validate_uniqueness_active()
        super(Agent, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.validate_uniqueness_active()
        super(Agent, self).update(*args, **kwargs)

    def __str__(self):
        return self.name


class Metric(models.Model):
    name = models.CharField('Nombre', max_length=100)
    value = models.CharField('Valor', max_length=100)
    metric_id = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name="Metrica")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Metrica'
        verbose_name_plural = 'Metricas'

    def __str__(self):
        return self.name