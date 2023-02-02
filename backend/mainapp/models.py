from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=16, default='')
    link = models.CharField(max_length=16, default='')

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'меню'

    def __str__(self):
        return f'{self.name}'
