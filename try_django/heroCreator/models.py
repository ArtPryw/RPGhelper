from django.db import models
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL

class Hero(models.Model):

    user        = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    name        = models.CharField(max_length=30)
    nickname    = models.CharField(max_length=30)
    race        = models.CharField(max_length=30)
    profession  = models.CharField(max_length=30)

    #To do ogarnięcia bo nie działa.
    slug        = models.SlugField(unique=True)

    strength    = models.PositiveSmallIntegerField()
    mana        = models.PositiveSmallIntegerField()
    HP          = models.PositiveSmallIntegerField()

    level       = models.PositiveSmallIntegerField(default = 0)
