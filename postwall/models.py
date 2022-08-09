from django.db import models

from accounts.helpers.models import TrackingModel
from accounts.models import User

# Create your models here.

class PostWall(TrackingModel, models.Model):
    title=models.CharField(max_length=100, default='')
    content = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
