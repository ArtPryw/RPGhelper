from django.db import models

# Create your models here.
class Hero(models.Model):
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
