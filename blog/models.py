from django.db import models
import datetime
from django.db.models.fields import URLField


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
    title_1 = models.CharField(max_length=100, default='')
    description_1 = models.TextField(default='')
    title_2 = models.CharField(max_length=100, default='')
    description_2 = models.CharField(max_length=999, default='')
    url3 = URLField(blank=True)
