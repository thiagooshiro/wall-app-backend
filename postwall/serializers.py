from rest_framework import serializers

from postwall.models import PostWall


class PostWallSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    title = serializers.CharField(required=False, default="")

    class Meta:
        model = PostWall
        fields = ['id', 'title', 'content', 'owner']
