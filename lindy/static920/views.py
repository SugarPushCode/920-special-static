from __future__ import absolute_import

# Standard Library
from datetime import datetime

# External Libraries
from django.conf import settings
from django.utils.functional import cached_property
from django.views.generic import TemplateView

# Project Library
from toolz import first

from lindy.static920.models.people import (
    DJS,
    PEOPLE,
    TEACHERS,
)


class DateItem(dict):

    @property
    def hide(self):
        return (
            self.get('hide', False)
            or (self.date and self.date < datetime.now().date())
        )

    @cached_property
    def date(self):
        return datetime.strptime(self['date'], "%m/%d/%Y").date() if 'date' in self else None


class NewsItem(DateItem):

    @property
    def hide(self):
        return super(NewsItem, self).hide or not self.get('content')


class BaseView(TemplateView):

    @property
    def db(self):
        return settings.HACK_DB


class Index(BaseView):
    template_name = 'index.jinja'

    def get_context_data(self, **kwargs):
        news = [
            news
            for news
            in map(NewsItem, self.db['news'])
            if not news.hide
        ]

        # get the names of the djs this week
        # filter djs down to ones that are today or in the future and pick the min date
        djs = min(
            (djs for djs in map(DateItem, self.db['djs']) if not djs.hide),
            key=lambda x: x.date
        ).get('names', ['TBD'])  # default to a "TBD" state

        return {
            'djs': djs,
            'schedule': self.db['schedule'],
            'news': news,
        }


class About(BaseView):
    template_name = 'about.jinja'


class Classes(BaseView):
    template_name = 'classes.jinja'

    def get_context_data(self, **kwargs):
        return {'teachers': TEACHERS}


class Dance(BaseView):
    template_name = 'dance.jinja'

    def get_context_data(self, **kwargs):
        return {
            # show the next four djs
            'djs': [djs for djs in map(DateItem, self.db['djs']) if not djs.hide][:4]
        }


class Music(BaseView):
    template_name = 'music.jinja'

    def get_context_data(self, **kwargs):
        return {'djs': DJS}


class Volunteers(BaseView):
    template_name = 'volunteers.jinja'
