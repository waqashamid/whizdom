from rest_framework import status, views
from rest_framework.response import Response
from django.db import DatabaseError
from django.shortcuts import render
from rest_framework.settings import api_settings
from .serializers import CardSerializer
from .models import *
from bouncer.models import *
from rest_framework import viewsets
from content.models import *

class BaseCardViewSet(viewsets.ModelViewSet):
    """
    A list of the latest content fetched in reverse chronological order
    """
    model = Card
    serializer_class = CardSerializer
    queryset = Card.objects.all()