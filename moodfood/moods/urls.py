from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mood_type>[0-9]+)/$', views.moodDetail, name='MoodDetail'),
    url(r'^(?P<mood_type>[0-9]+)/restaurantRec/$', views.restaurantRec, name='restaurantRec'),
    url(r'^(?P<mood_type>[0-9]+)/restaurantApprove/$', views.restaurantApprove, name='restaurantApprove'),
]
