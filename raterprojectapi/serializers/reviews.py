from rest_framework import serializers
from raterprojectapi.models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        player = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        game = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        fields = ('id', 'review', 'player', 'game', 'datestamp')
        depth = 0
