from rest_framework import status, views
from rest_framework.response import Response
from django.db import DatabaseError
from django.shortcuts import render
from rest_framework.settings import api_settings
from .serializers import CardSerializer
from .models import *
from bouncer.models import *

class FetchUserCards(views.APIView):

    def get(self, request, **kwargs):
        # Incorrect TODO: fix
        try:
            user = User.objects.get(id=str(kwargs.get(id)))
        except (User.DoesNotExist, KeyError) as e:
            return Response({"error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        cards = Card.objects.all()
        filtered_cards = []
        for card in cards:
            if card not in user.cards_seen:
                filtered_cards.append(card)
        return Response([CardSerializer(card).data for card in filtered_cards], status=status.HTTP_200_OK)