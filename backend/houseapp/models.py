from django.db import models
from django.urls import reverse


# Create your models here.
class Nodemcu(models.Model):
    title = models.CharField(max_length=50, default='')
    urls = models.TextField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('node_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'действие'
        verbose_name_plural = 'действия с NodeMCU'


class PartString(models.Model):
    name = models.CharField(max_length=32, default='')
    body = models.TextField(default='')

    def __str__(self):
        return f'{self.name} - {self.body}'

    class Meta:
        verbose_name = 'фраза'
        verbose_name_plural = 'частые фразы'
