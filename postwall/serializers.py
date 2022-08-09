from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from postwall.models import PostWall


class PostWallSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = PostWall
        fields = ['title', 'content', 'owner']