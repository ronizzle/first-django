from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=5, max_digits=5)

