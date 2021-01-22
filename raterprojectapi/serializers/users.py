from rest_framework import serializers
from raterprojectapi.models import Players
from django.contrib.auth import get_user_model


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        user = get_user_model()
        fields = ('id', 'user', 'name', 'age')
        depth = 3
