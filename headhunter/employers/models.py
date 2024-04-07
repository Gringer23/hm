from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from applicants.models import Position


class Employers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Работодатели'


class Vacancies(models.Model):
    employers = models.ForeignKey(Employers, on_delete=models.CASCADE, verbose_name='Работодатель')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True,verbose_name='Описание вакансии')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Вакансии'

class ResponseVacancies(models.Model):
    employers = models.ForeignKey(Employers, on_delete=models.CASCADE, verbose_name='Работодатель')
    vacancies = models.ForeignKey(Vacancies, on_delete=models.CASCADE, verbose_name='Вакансия', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Соискатель')
    date = models.DateTimeField(auto_now=True)
    is_invitation = models.BooleanField(default=False, verbose_name='Приглашение на собеседование')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность", null=True, blank=True)

    def __str__(self):
        return f'{self.employers.title} - {self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = 'Отлик на вакансию'