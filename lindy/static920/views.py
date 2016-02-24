from __future__ import absolute_import

# External Libraries
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.jinja'


class About(TemplateView):
    template_name = 'about.jinja'


class Classes(TemplateView):
    template_name = 'classes.jinja'

class Dance(TemplateView):
    template_name = 'dance.jinja'

class Music(TemplateView):
    template_name = 'music.jinja'

class Volunteers(TemplateView):
    template_name = 'volunteers.jinja'
