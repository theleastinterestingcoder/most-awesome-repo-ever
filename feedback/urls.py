from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Note: I don't know why these url patterns need to start with '/' while the other ones don't
# Don't use this as an example of what to do. 
urlpatterns = patterns('',
    url(
        r'/feedback_form', 
        'feedback.views.feedback', 
        name='feedback'),
    url(
        r'/feedback_thanks', 
        'feedback.views.thanks', 
        name='feedback_thanks'),
    url(
        r'/feedback_responses', 
        'feedback.views.responses', 
        name='feedback_responses'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
