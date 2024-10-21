import datetime

from django.db import models


class Record(models.Model):
    uuid = models.UUIDField(primary_key=True)
    h1 = models.IntegerField(default=0)
    h2 = models.IntegerField(default=0)
    h3 = models.IntegerField(default=0)
    a = models.JSONField()
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)
    def __str__(self):
        return self.uuid
