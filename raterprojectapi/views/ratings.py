from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterprojectapi.models import Games, Players, Ratings
from raterprojectapi.serializers import RatingSerializer
import datetime

class RatingsViewSet(ViewSet):
    def create(self, request):
        rating = Ratings()
        rating.rating_value = request.data["rating"]
        rating.player = Players.objects.get(pk=request.data["player"])
        rating.game = Games.objects.get(pk=request.data["game"])


        try:
            rating.save()
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            rating = Ratings.objects.get(pk=pk)
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        rating = Ratings.objects.get(pk=pk)
        rating.player = rating.player
        rating.game = rating.game
        rating.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            rating = Ratings.objects.get(pk=pk)
            rating.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Ratings.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        ratings = Ratings.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games

        serializer = RatingSerializer(
            ratings, many=True, context={'request': request})
        return Response(serializer.data)
