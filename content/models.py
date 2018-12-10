from django.db import models
from bouncer.mixins import BaseModelMixin
from uuid import uuid4

class Media(BaseModelMixin):
    """
    Holds the media being used in the platform
    """
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Name', default='whizdom')
    is_image = models.BooleanField(default=False, verbose_name='is_image')
    is_video = models.BooleanField(default=False, verbose_name='is_video')
    image = models.ImageField(null=True, blank=True, verbose_name='Image')
    video = models.TextField(null=True, blank=True, verbose_name='Video')

    def __str__(self):
        return self.name


class Card(BaseModelMixin):
    """
    Holds the card models
    """
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Name', default='whizdom')
    body = models.TextField(null=False, blank=False, verbose_name='Body', default='whizdom')
    headline = models.CharField(max_length=256, null=False, blank=False, verbose_name='Headline', default='whizdom')
    media = models.ManyToManyField(Media, verbose_name='Media', blank=True)

    def __str__(self):
        return self.name