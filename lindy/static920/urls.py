# -*- coding: utf-8 -*-

from __future__ import absolute_import

# External Libraries
from django.conf.urls import url

from .views import (
    About,
    Classes,
    Contact,
    Dance,
    Index,
    Music,
    Volunteers,
    Survey,
)

urlpatterns = [
    url(r'^about', About.as_view()),
    url(r'^classes', Classes.as_view()),
    url(r'^dance', Dance.as_view()),
    url(r'^music', Music.as_view()),
    url(r'^volunteers', Volunteers.as_view()),
    url(r'^survey', Survey.as_view()),
    url(r'^contact/?', Contact.as_view()),
    url(r'^$', Index.as_view()),
]
