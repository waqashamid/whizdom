from rest_framework import status, views
from rest_framework.response import Response
from django.db import DatabaseError
from django.shortcuts import render
from rest_framework.settings import api_settings
from .serializers import CardSerializer
from .models import *

class FetchCards(views.APIView):

    def get(self, request, **kwargs):
        cards = Card.objects.all()
        return Response([CardSerializer(card).data for card in cards], status=status.HTTP_200_OK)