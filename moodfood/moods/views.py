from django.http import HttpResponse
from django.shortcuts import render
from .models import Type, Restaurant, Mood
import random


def moodDetail(request, mood_type):
    mood = Mood.objects.get(pk=mood_type)
    return HttpResponse("You're looking at mood %s." % mood)


def restaurantRec(request, mood_type):
    moo = Mood.objects.get(pk=mood_type)
    recNum = moo.restaurant_list.count()
    randNum = random.randint(0, recNum-1)
    response = "Your reccomendation for your mood is %s."
    return HttpResponse(response % moo.restaurant_list.all()[randNum])


def restaurantApprove(request, mood_type):
    return HttpResponse("You're deciding on a restauarnt for %s." % mood_type)


def index(request):
    return render(request, 'moods/moods.html')