from django.db import models
import uuid
from datetime import date


class User(models.Model):
    full_name = models.CharField(max_length=100)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE)
    is_fired = models.BooleanField(default=False)
    fire_date = models.DateTimeField(default=date.today)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.full_name


class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=100)

    def __str__(self):
        return self.vacancy_name
