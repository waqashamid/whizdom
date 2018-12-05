from django.conf.urls import url
from .api import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'(?P<user_id>[\w.-]+)/', FetchUserCards.as_view(), name='get_content'),
]
