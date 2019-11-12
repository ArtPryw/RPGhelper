from django.db import models
from django.conf import settings
import random
# Create your models here.


User = settings.AUTH_USER_MODEL

class Hero(models.Model):

    def strengthRandomizer():
        str_random = random.randint(1,20)
        return str_random

    def manaRandomizer():
        mana_random = random.randint(1,100)
        return mana_random

    def hpRandomizer():
        HP_random = random.randint(1,30)
        return HP_random

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

    strength    = models.PositiveSmallIntegerField(default=strengthRandomizer)
    mana        = models.PositiveSmallIntegerField(default=manaRandomizer)
    HP          = models.PositiveSmallIntegerField(default=hpRandomizer)

    level       = models.PositiveSmallIntegerField(default = 0)



    def get_absolute_url(self):
        return f"/heroes/{self.slug}/"

    def get_edit_url(self):
        return f"/heroes/{self.slug}/edit/"

    def get_delete_url(self):
        return f"/heroes/{self.slug}/delete/"
