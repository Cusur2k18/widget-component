# Generated by Django 2.2.1 on 2019-05-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widget', '0003_auto_20190530_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric',
            name='level',
        ),
        migrations.AddField(
            model_name='agent',
            name='level',
            field=models.IntegerField(default=0, verbose_name='Nivel'),
        ),
        migrations.AddField(
            model_name='metric',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Activa'),
        ),
    ]
