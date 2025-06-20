# Generated by Django 5.2.1 on 2025-05-12 16:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reclamos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('resuelto', 'Resuelto')], default='pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='ticket',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=10, unique=True),
        ),
    ]
