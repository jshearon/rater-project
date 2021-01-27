from rest_framework import serializers
from raterprojectapi.models import Ratings
from rest_framework.validators import UniqueTogetherValidator

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        validators = [
            UniqueTogetherValidator(
                queryset=Ratings.objects.all(),
                fields=['player', 'game'],
                message="This player has already rated this game"
            )
        ]
        player = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        game = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        fields = ('id', 'rating_value', 'player', 'game')
        depth = 0
