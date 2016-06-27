from __future__ import absolute_import

# Standard Library
from datetime import (
    datetime,
    timedelta,
)
from textwrap import dedent

# External Libraries
import sendgrid
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.functional import cached_property
from django.views.generic import (
    TemplateView,
    View,
)

# Project Library
from lindy.static920.models.people import (
    DJS,
    TEACHERS,
)


def now():
    from pytz import timezone
    local = timezone('US/Pacific')
    return datetime.now(local)

def this_month(format='%m/%Y'):
    return now().strftime(format)

def next_month(format='%m/%Y'):
    return (now().replace(day=28) + timedelta(days=4)).strftime(format)

class DateItem(dict):

    @property
    def hide(self):
        return (
            self.get('hide', False)
            or (self.date and self.date < now().date())
        )

    @cached_property
    def date(self):
        if "date" in self:
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
        djs = [djs for djs in map(DateItem, self.db['djs']) if not djs.hide]
        if djs:
            djs = min(djs, key=lambda x: x.date).get('names', ['TBD'])  # default to a "TBD" state
        else:
            djs = ['TBD']

        return {
            'djs': djs,
            'schedule': settings.TEACHER_SCHEDULE.get(this_month()),
            'news': news,
        }


class About(BaseView):
    template_name = 'about.jinja'


class Classes(BaseView):
    template_name = 'classes.jinja'

    def get_context_data(self, **kwargs):
        return {
            'teachers': TEACHERS
        }


class Dance(BaseView):
    template_name = 'dance.jinja'

    def get_context_data(self, **kwargs):
        return {
            # show the next four djs
            'djs': [djs for djs in map(DateItem, self.db['djs']) if not djs.hide][:4],
            'this_month': this_month('%B'),
            'next_month': next_month('%B'),
            'schedule_this_month': settings.TEACHER_SCHEDULE.get(this_month()),
            'schedule_next_month': settings.TEACHER_SCHEDULE.get(next_month()),
        }


class Music(BaseView):
    template_name = 'music.jinja'

    def get_context_data(self, **kwargs):
        return {'djs': DJS}


class Volunteers(BaseView):
    template_name = 'volunteers.jinja'


class Contact(View):

    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        reason = request.POST.get('reason')
        reason_word = reason.split()[-1]
        message = request.POST.get('message')
        email = request.POST.get('email')
        next = request.GET.get('next', '/')

        text = dedent('''\
        Who:

        {name} ({email})

        Reason:

        {reason}

        Message:

        {message}
        '''.format(name=name, reason=reason, message=message, email=email,))

        subject = '[{reason}] {subject}...'.format(reason=reason_word, subject=message[:50])

        sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)

        sg_message = sendgrid.Mail()
        sg_message.add_to(settings.CONTACT_EMAIL)
        sg_message.set_from(email)
        sg_message.set_from_name(name)
        sg_message.set_subject(subject)
        sg_message.set_text(text)
        sg.send(sg_message)

        return HttpResponseRedirect(next)
