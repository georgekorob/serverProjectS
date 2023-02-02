import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from mainapp.models import MenuItem


# Create your models here.
class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    birth = models.DateField(default=datetime.date.today)
    about = models.TextField(verbose_name='о себе', default='')
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES, default=MALE, max_length=2)
    menu_access = models.ManyToManyField(MenuItem)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
