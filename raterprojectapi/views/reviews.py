from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterprojectapi.models import Games, Players, Reviews
from raterprojectapi.serializers import ReviewSerializer
import datetime

class ReviewsViewSet(ViewSet):
    def create(self, request):
        review = Reviews()
        review.review = request.data["review"]
        review.player = Players.objects.get(pk=request.data["player"])
        review.game = Games.objects.get(pk=request.data["game"])
        review.datestamp = datetime.datetime.now()


        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            review = Reviews.objects.get(pk=pk)
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        review = Reviews.objects.get(pk=pk)
        review.review = request.data["review"]
        review.player = Players.objects.get(pk=request.data["player"])
        review.game = Games.objects.get(pk=request.data["game"])
        review.datetime = review.datetime
        review.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            review = Reviews.objects.get(pk=pk)
            review.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Reviews.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        reviews = Reviews.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)
