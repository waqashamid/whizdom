from django.core.management.base import BaseCommand
from bouncer.models import User
from bouncer.constants import ROOT_EMAIL, ROOT_PASSWORD
import logging

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        if not User.objects.filter(email=ROOT_EMAIL).exists():
            User.objects.create_superuser(ROOT_EMAIL, password=ROOT_PASSWORD, )
            logger.info("Primary super user created")