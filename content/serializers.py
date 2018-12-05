from rest_framework import serializers
from . import models

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'created', 'modified', 'name', 'image', 'video')
        model = models.Media

class CardSerializer(serializers.ModelSerializer):

    media = MediaSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'name', 'created', 'modified', 'body', 'headline', 'media')
        model = models.Card