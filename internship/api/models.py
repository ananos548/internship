from django.db import models
from datetime import datetime


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField(default=datetime)


class InvestmentProjects(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
