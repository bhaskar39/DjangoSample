from __future__ import unicode_literals

from django.db import models

# Create your models here.

class post_data(models.Model):
    user = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    post_head = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    post_date = models.DateTimeField('date posted')

