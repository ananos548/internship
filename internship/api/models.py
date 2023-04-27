from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.title}'


class InvestmentProject(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
