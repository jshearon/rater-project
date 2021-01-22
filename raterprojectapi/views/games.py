from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterprojectapi.models import Games, Players, Categories
from raterprojectapi.serializers import GameSerializer

class GamesViewSet(ViewSet):
    def create(self, request):
        player = Players.objects.get(user=request.auth.user)

        game = Games()
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.year_released = request.data["year_released"]
        game.total_players = request.data["total_players"]
        game.duration = request.data["duration"]
        game.age_restriction = request.data["age_restriction"]
        game.player_id = player

        gamecat = Categories.objects.get(pk=request.data["gameCatId"])
        game.gamecat = gamecat

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        try:
            game = Games.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        player = Players.objects.get(user=request.auth.user)

        game = Games.objects.get(pk=pk)
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.year_released = request.data["year_released"]
        game.total_players = request.data["total_players"]
        game.duration = request.data["duration"]
        game.age_restriction = request.data["age_restriction"]
        game.player_id = player

        gamecat = Categories.objects.get(pk=request.data["categoryId"])
        game.gamecat = gamecat
        game.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            game = Games.objects.get(pk=pk)
            game.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Games.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        games = Games.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        gamecat = self.request.query_params.get('type', None)
        if gamecat is not None:
            games = games.filter(gamecat__id=gamecat)

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)
