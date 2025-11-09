from django.db import models


class SheepCounter(models.Model):
    count = models.IntegerField(default=0)
