from django.conf.urls import url
from .api import *
from django.views.decorators.csrf import csrf_exempt

# (?P<user_id>[\w.-]+)
urlpatterns = [
    url(r'', BaseCardViewSet.as_view({'get': 'list', }, name='card-details')),
]
