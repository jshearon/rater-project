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
  categories = models.ManyToManyField("Categories",
      related_name="game_categories",
      related_query_name="game_category"
    )
  
  @property
  def average_rating(self):
    from raterprojectapi.models import Ratings
    """Average rating calculated attribute for each game"""
    ratings = Ratings.objects.filter(game=self)

    # Sum all of the ratings for the game
    total_rating = 0
    for rating in ratings:
        total_rating += rating.rating_value

    if len(ratings) is not 0:
      return total_rating/len(ratings)
    else:
      return 0

    # Calculate the averge and return it.
    # If you don't know how to calculate averge, Google it.
