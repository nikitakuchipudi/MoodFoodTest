from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mood_type>[a-z]+)/$', views.moodDetail, name='MoodDetail'),
    url(r'^(?P<mood_type>[a-z]+)/restaurantRec/$', views.restaurantRec, name='restaurantRec'),
    url(r'^(?P<mood_type>[a-z]+)/restaurantApprove/$', views.restaurantApprove, name='restaurantApprove'),
]
