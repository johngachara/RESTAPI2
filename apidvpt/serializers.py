from rest_framework import serializers

from apidvpt.models import Artist


class Artistserializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name','phone','email']

class AtristAlbumserializer(serializers.ModelSerializer):
    artists = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Artist
        fields = ['name','email','artists']