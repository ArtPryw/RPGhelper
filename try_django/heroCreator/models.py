from django.db import models

# Create your models here.
class Hero(models.Model):
    name        = models.TextField(null = True, blank = True)
    nickname    = models.TextField(null = True, blank = True)
    race        = models.TextField(null = True, blank = True)
    profession  = models.TextField(null = True, blank = True)

    strength    = models.PositiveSmallIntegerField()
    mana        = models.PositiveSmallIntegerField()
    HP          = models.PositiveSmallIntegerField()
