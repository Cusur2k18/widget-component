# Generated by Django 2.2.1 on 2019-06-06 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widget', '0009_auto_20190606_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='agent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='widget.Agent', verbose_name='Agent'),
        ),
    ]
