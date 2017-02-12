from django.http import HttpResponse
from django.shortcuts import render
from .models import Type, Restaurant, Mood
import random


def moodDetail(request, mood_type):
    mood = Mood.objects.get(mood_name__contains=mood_type)
    return HttpResponse("You're looking at mood %s." % mood)


def restaurantRec(request, mood_type):
    moo = Mood.objects.get(mood_name__contains=mood_type)
    recNum = moo.restaurant_list.count()
    randNum = random.randint(0, recNum-1)
    rec = moo.restaurant_list.all()[randNum]
    response = "Your recommendation for your mood is %s."
    context = {'rec': rec}
    return render(request, 'moods/rec.html', context)


def restaurantApprove(request, mood_type):
    return HttpResponse("You're deciding on a restauarnt for %s." % mood_type)


def index(request):
    return render(request, 'moods/moods.html')