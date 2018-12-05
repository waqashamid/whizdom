from django.db import models
from uuid import uuid4

class BaseModelMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    id = models.CharField(primary_key=True, default=str(uuid4()), editable=False, max_length=36, unique=True)

    class Meta:
        abstract = True
