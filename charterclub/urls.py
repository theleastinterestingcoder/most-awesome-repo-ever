from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#Here is a mapping between the pattern in the URL to the function that
#   generates the page.
urlpatterns = patterns('',
    url(
        r'^$',
        'charterclub.views.index',
        name='index'), 

    url(
        r'^index$',
        'charterclub.views.index',
        name='index'),
    url(
        r'^calendar$',
        'charterclub.views.calendar',
        name='calendar'),
    url(
        r'^menu$',
        'charterclub.views.menu',
        name='menu'),
    url(
        r'^history$',
        'charterclub.views.history',
        name='history'),
    url(
        r'^song$',
        'charterclub.views.song',
        name='song'),
    url(
        r'^constitution$',
        'charterclub.views.constitution',
        name='constitution'),
    url(
        r'^#$',
        'charterclub.views.underconstruction',
        name='#')
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)