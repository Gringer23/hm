# Generated by Django 5.0.3 on 2024-04-05 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_position_cv_position_resume'),
        ('employers', '0004_responsevacancies_is_invitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsevacancies',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='applicants.position', verbose_name='Должность'),
        ),
    ]
