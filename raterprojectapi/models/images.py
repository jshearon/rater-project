from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class GameImages(models.Model):
    image = models.ImageField(upload_to ='uploads/')
    player = models.ForeignKey("Players",
      on_delete=CASCADE,
      related_name="gameimages",
      related_query_name="gameimage"
    )
    game = models.ForeignKey("Games",
      on_delete=CASCADE,
      related_name="gameimages",
      related_query_name="gameimage"
    )
