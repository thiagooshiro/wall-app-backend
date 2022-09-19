from django.db import models

from accounts.helpers.models import TrackingModel
from accounts.models import User


class PostWall(TrackingModel, models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    content = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
