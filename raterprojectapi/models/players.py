from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Players(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.TextField()
    age = models.IntegerField()
