from django.db import models


class Type(models.Model):
    """
    Restaurant type
    """
    word = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.word


class Restaurant(models.Model):
    """
    Restaurant model. Name, address, type
    """
    restaurant_name = models.CharField(max_length=100, null=True)
    restaurant_address = models.CharField(max_length=100, null=True)
    restaurant_type = models.ManyToManyField(Type)
    def __str__(self):
        return self.restaurant_name


class Mood(models.Model):
    """
    Mood model. Name, restaurant list.
    """
    mood_name = models.CharField(max_length=20, null=True)
    restaurant_list = models.ManyToManyField(Restaurant)
    def __str__(self):
        return self.mood_name
