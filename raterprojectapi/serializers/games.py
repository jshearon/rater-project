from rest_framework import serializers
from raterprojectapi.models import Games

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'maker', 'number_of_players', 'skill_level', 'gamecat')
        depth = 1
