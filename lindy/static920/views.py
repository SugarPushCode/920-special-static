from __future__ import absolute_import

# Standard Library
from datetime import datetime

# External Libraries
from django.conf import settings
from django.utils.functional import cached_property
from django.views.generic import TemplateView

# Project Library
from lindy.static920.models.people import (
    DJS,
    PEOPLE,
    TEACHERS,
)


class NewsItem(dict):

    @property
    def hide(self):
        return (
            self.get('hide', False)
            or (self.date and self.date <= datetime.now().date())
            or not self.get('content')
        )

    @cached_property
    def date(self):
        return datetime.strptime(self['date'], "%m/%d/%Y").date() if 'date' in self else None

class BaseView(TemplateView):

    @property
    def db(self):
        print(settings.HACK_DB)
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
        print(news)
        return {
            'dj1': PEOPLE[self.db['djs'][0]],
            'dj2': PEOPLE[self.db['djs'][1]],
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


class Music(BaseView):
    template_name = 'music.jinja'

    def get_context_data(self, **kwargs):
        return {'djs': DJS}


class Volunteers(BaseView):
    template_name = 'volunteers.jinja'
