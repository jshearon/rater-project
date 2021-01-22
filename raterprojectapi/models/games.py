from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Games(models.Model):
  title = models.CharField(max_length=75)
  description = models.TextField()
  designer = models.CharField(max_length=75)
  year_released = models.IntegerField()
  total_players = models.IntegerField()
  duration = models.IntegerField()
  age_restriction = models.IntegerField()
  player_id = models.ForeignKey("Players", 
    on_delete=CASCADE,
    related_name="players",
    related_query_name="player")
  gamecat = models.ManyToManyField("Categories",
      related_name="game_categories",
      related_query_name="game_category"
    )
