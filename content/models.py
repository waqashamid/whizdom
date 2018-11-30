from django.db import models
from bouncer.models import Base
from uuid import uuid4

# Create your models here.

class Card(Base):

    id = models.CharField(uuid4(), primary_key=True, unique=True, max_length=50)
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Name', default='whizdom')
    body = models.TextField(null=False, blank=False, verbose_name='Body', default='whizdom')
    headline = models.CharField(max_length=256, null=False, blank=False, verbose_name='Headline', default='whizdom')

    def __str__(self):
        return self.name

class Media(Base):

    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Name', default='whizdom')
    card = models.ManyToManyField(Card, verbose_name='Card')
    image = models.ImageField(null=True, blank=True, verbose_name='Image')
    video = models.TextField(null=True, blank=True, verbose_name='Video')

    def __str__(self):
        return self.name