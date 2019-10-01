from django.db import models

# Create your models here.
class Hero(models.Model):
    name        = models.TextField(null = True, blank = True)
    nickname    = models.TextField(null = True, blank = True)
    race        = models.TextField(null = True, blank = True)
    profession  = models.TextField(null = True, blank = True)

    #To do ogarnięcia bo nie działa.
    #slug        = models.SlugField(default = 'this-is-my-slug')

    strength    = models.PositiveSmallIntegerField()
    mana        = models.PositiveSmallIntegerField()
    HP          = models.PositiveSmallIntegerField()
