from __future__ import unicode_literals

from django.apps import AppConfig


class Task1Config(AppConfig):
    name = 'seedstar_django_challenge.task1'
    verbose_name = "Task1"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

