from django.db import models
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL

class Hero(models.Model):
    RACES = {
    (0, "None"),
    (0, "Human"),
    (0, "Elf"),
    (0, "Dwarf"),
    (0, "Ogre"),
    (0, "Hobbit"),
    (0, "Gnome"),
    }


    user        = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    name        = models.CharField(max_length=30)
    nickname    = models.CharField(max_length=30)
    race        = models.IntegerField(default=0, choices=RACES)
    profession  = models.CharField(max_length=30)

    #To do ogarnięcia bo nie działa.
    slug        = models.SlugField(unique=True)

    strength    = models.PositiveSmallIntegerField()
    mana        = models.PositiveSmallIntegerField()
    HP          = models.PositiveSmallIntegerField()

    level       = models.PositiveSmallIntegerField(default = 0)



    def get_absolute_url(self):
        return f"/heroes/{self.slug}/"

    def get_edit_url(self):
        return f"/heroes/{self.slug}/edit/"

    def get_delete_url(self):
        return f"/heroes/{self.slug}/delete/"
