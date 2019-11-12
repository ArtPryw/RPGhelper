from django.db import models
from django.conf import settings
import random
# Create your models here.


User = settings.AUTH_USER_MODEL

class Hero(models.Model):
    RACES = {
    ("None", "None"),
    ("Human", "Human"),
    ("Elf", "Elf"),
    ("Dwarf", "Dwarf"),
    ("Ogre", "Ogre"),
    ("Hobbit", "Hobbit"),
    ("Gnome", "Gnome"),
    }


    user        = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    name        = models.CharField(max_length=30)
    nickname    = models.CharField(max_length=30)
    race        = models.CharField(default=0, choices=RACES, max_length = 30)
    profession  = models.CharField(max_length=30)

    #To do ogarnięcia bo nie działa.
    slug        = models.SlugField(unique=True)

    strength    = models.PositiveSmallIntegerField(default=1)
    mana        = models.PositiveSmallIntegerField(default=1)
    HP          = models.PositiveSmallIntegerField(default = 1)

    level       = models.PositiveSmallIntegerField(default = 0)



    def get_absolute_url(self):
        return f"/heroes/{self.slug}/"

    def get_edit_url(self):
        return f"/heroes/{self.slug}/edit/"

    def get_delete_url(self):
        return f"/heroes/{self.slug}/delete/"
