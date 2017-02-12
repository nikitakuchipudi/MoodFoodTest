from django.contrib import admin

from .models import Restaurant, Mood, Type

admin.site.register(Restaurant)

admin.site.register(Mood)

admin.site.register(Type)