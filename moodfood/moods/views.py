from django.http import HttpResponse
from django.shortcuts import render
from .models import Type, Restaurant, Mood


def moodDetail(request, mood_type):
    return HttpResponse("You're looking at mood %s." % Mood.objects.get(pk=mood_type))


def restaurantRec(request, mood_type):
    response = "You're looking at the recommendations of mood %s."
    return HttpResponse(response % mood_type)


def restaurantApprove(request, mood_type):
    return HttpResponse("You're deciding on a restauarnt for %s." % mood_type)


def index(request):
    return render(request, 'moods/moods.html')