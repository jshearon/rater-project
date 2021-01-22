from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Categories(models.Model):
    label = models.CharField(max_length=100) 
