from django.db import models
from datetime import datetime
from django.db.models.aggregates import Count
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

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
    





@receiver(post_save, sender=Rating)
def calculate_rating(sender, instance, **kwargs):
    """
    This Function is called everytime there is a change in Rating table
    """
    channel_id = instance.channel_id

    total = Rating.objects.filter(channel_id= channel_id).count()
    queryset = Rating.objects.filter(channel_id= channel_id)
    total_sum =0
    for i in queryset:
        total_sum += i.rating


    print(total, total_sum)

    channel = Channel.objects.filter(id= channel_id.id).first()
    channel.rate =  int(total_sum/total)
    channel.save()

