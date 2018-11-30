from rest_framework import serializers
from . import models

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'created', 'modified', 'body', 'headline', )
        model = models.Card