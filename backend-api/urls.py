from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from api.views import *
from django.urls import path
from .views import movie_times
from .views import movie_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('movietimes/', movie_times, name='movie_times'),
    path('movielist/', movie_list, name='movie_list'),

]
