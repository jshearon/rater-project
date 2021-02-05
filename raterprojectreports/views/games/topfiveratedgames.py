"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from raterprojectapi.models import Games, Ratings
from raterprojectreports.views import Connection


def topfivegames_list(request):
    """Function to build an HTML report of games by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT
                  SUM(r.rating_value) total_rating, 
                  g.*
                FROM
                    raterprojectapi_ratings r
                JOIN 
                    raterprojectapi_games g ON g.id = r.game_id
                GROUP BY g.id
                ORDER BY total_rating DESC
            """)

            dataset = db_cursor.fetchall()

            # {
            #  1: {
            #      "gamer_id": 1,
            #      "full_name": "Molly Ringwald",
            #      "events": [
            #          {
            #              "id": 5,
            #              "date": "2020-12-23",
            #              "time": "19:00",
            #              "game_name": "Fortress America"
            #          }
            #      ]
            #  }
            #}

            games_by_rating = {}

            for row in dataset:
              uid = row["id"]
              # Otherwise, create the key and dictionary value
              games_by_rating[uid] = {}
              games_by_rating[uid]["id"] = uid
              games_by_rating[uid]["title"] = row["title"]
              games_by_rating[uid]["total_rating"] = row["total_rating"]

        # Get only the values from the dictionary and create a list from them
        list_of_top_five_games = games_by_rating.values()

        # Specify the Django template and provide data context
        template = 'games/list_with_top_five_games.html'
        context = {
            'topfivegames_list': list_of_top_five_games
        }

        return render(request, template, context)
