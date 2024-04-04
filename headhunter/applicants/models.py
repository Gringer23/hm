from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, null=True, blank=True)
    resume = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    cv = models.FileField(upload_to='cv/', blank=True, null=True, verbose_name='CV')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.title}'

    class Meta:
        verbose_name_plural = 'Соискатель'