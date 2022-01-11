from django.db import models
from datetime import datetime

from django.db.models import constraints

from users.models import User
from channels.models import Channel

# Create your models here.
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['channel_id','user_id'], name='Rating'
            )
        ]
    

