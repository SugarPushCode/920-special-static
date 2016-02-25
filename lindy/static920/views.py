from __future__ import absolute_import

# External Libraries
from django.views.generic import TemplateView

# Project Library
from lindy.static920.models.people import (
    DJS,
    TEACHERS,
    THIS_WEEK,
)


class Index(TemplateView):
    template_name = 'index.jinja'

    def get_context_data(self, **kwargs):
        return {
            'dj1': THIS_WEEK['dj1'],
            'dj2': THIS_WEEK['dj2'],
        }


class About(TemplateView):
    template_name = 'about.jinja'


class Classes(TemplateView):
    template_name = 'classes.jinja'

    def get_context_data(self, **kwargs):
        return {'teachers': TEACHERS}


class Dance(TemplateView):
    template_name = 'dance.jinja'


class Music(TemplateView):
    template_name = 'music.jinja'

    def get_context_data(self, **kwargs):
        return {'djs': DJS}


class Volunteers(TemplateView):
    template_name = 'volunteers.jinja'
