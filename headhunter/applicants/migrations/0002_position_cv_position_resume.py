# Generated by Django 5.0.3 on 2024-04-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv/', verbose_name='CV'),
        ),
        migrations.AddField(
            model_name='position',
            name='resume',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]
