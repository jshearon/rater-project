from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Ratings(models.Model):
    rating_value = models.IntegerField()
    player = models.ForeignKey("Players",
      on_delete=CASCADE,
      related_name="ratings",
      related_query_name="rating"
    )
    game = models.ForeignKey("Games",
      on_delete=CASCADE,
      related_name="ratings",
      related_query_name="rating"
    )
