from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Reviews(models.Model):
    review = models.TextField()
    player = models.ForeignKey("Players",
      on_delete=CASCADE,
      related_name="reviews",
      related_query_name="review"
    )
    game = models.ForeignKey("Games",
      on_delete=CASCADE,
      related_name="reviews",
      related_query_name="review"
    )
    datestamp = models.DateTimeField()
