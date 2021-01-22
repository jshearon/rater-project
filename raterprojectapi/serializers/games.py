from rest_framework import serializers
from raterprojectapi.models import Games

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        url = serializers.HyperlinkedIdentityField(view_name='games')
        fields = ('id', 'url', 'title', 'description', 'designer', 'year_released', 'total_players', 'duration', 'age_restriction', 'categories')
        depth = 2
