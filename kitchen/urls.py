from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^weekly_menu$', 
        'kitchen.views.weekly_menu', 
        name='weekly_menu'),
    url(
        r'^meal_signup$', 
        'kitchen.views.meal_signup', 
        name='meal_signup'),
    
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
