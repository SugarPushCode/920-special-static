"""
Django settings for lindy.special920 project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import

# Standard Library
import os
from os import environ
import pprint

# External Libraries
import yaml
from django_jinja.backend import Jinja2
from django_jinja.builtins import DEFAULT_EXTENSIONS
from path import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = (Path(__file__).dirname() / '..').abspath()
PROJECT_ROOT = (BASE_DIR / '..').abspath()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5@l^^lozn5d41x1iiotg#=!g#osewcc1mf8x4em&u-htb-9eae'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(environ.get('DEBUG', 0))
print(DEBUG)
ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'lindy.static920',

    'pipeline',
    # 'djangobower',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lindy.special920.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'cache_size': 0,
            'match_extension': '',
            'match_regex': r'.*',
            'auto_reload': DEBUG,
            'extensions': DEFAULT_EXTENSIONS + [
                'pipeline.jinja2.PipelineExtension',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    },
    # {
    #     'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #     'DIRS': [],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         'context_processors': [
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.request',
    #             'django.contrib.auth.context_processors.auth',
    #             'django.contrib.messages.context_processors.messages',
    #         ],
    #     },
    # },
]

WSGI_APPLICATION = 'lindy.special920.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

SHOW_ERRORS_INLINE = False
PIPELINE = {
    'SHOW_ERRORS_INLINE': False,
    'STYLESHEETS': {
        'app': {
            'source_filenames': (
                'scss/app.scss',
            ),
            'output_filename': 'css/app.css',
        },
    },
    'COMPILERS': (
        'pipeline.compilers.sass.SASSCompiler',
    ),
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    # 'SASS_BINARY': PROJECT_ROOT / 'node_modules' / '.bin' / 'node-sass',
    'SASS_BINARY': '/usr/bin/env python -m sassc',
    'SASS_ARGUMENTS': ' '.join('-I {}'.format(d) for d in (
        PROJECT_ROOT / 'bower_components/foundation-sites/scss',
        PROJECT_ROOT / 'bower_components/motion-ui/src',
    ))
}


STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_ROOT / 'static'

HACK_DB = yaml.load(open(PROJECT_ROOT / 'data.yml'))

class_desc_dict = {
    'Level 1A': '6-count + 8-count',
    'Level 1B': '8-count + Charleston',
    'Level 1C': '6-count + Charleston',
    'Level 2A': 'Swingouts',
    'Level 2B': 'Musicality',
    'Level 2C': 'Charleston',
    'Level 2D': 'Classics',
    'Level 3A': 'Technique',
    'Level 3B': 'Musicality',
    'Level 3C': 'Beyond Lindy Hop',
    'Level 3D': 'Vocabulary',
    'Level 3P': 'Performance Class',
}

with open('teacher_schedule.csv') as schedule:
    from csv import reader

    lines = reader(schedule)
    header = list(map(str.strip, next(lines)))

    lines = [list(map(str.strip, line)) for line in lines if line]

    TEACHER_SCHEDULE = {}
    for line in lines:
        line = dict(zip(header, line))
        d = {}
        for key, value in line.items():
            if key.lower() == 'month':
                (month,year) = value.split('/')
                if int(month) < 10 and len(month) == 1: 
                    value = '0' + value
                TEACHER_SCHEDULE[value] = d
            else:
                # eg. Level 1@7:20
                name, time = key.split('@')

                # In the instructor field of the CSV file,
                # prepend with the class letter and a colon
                # eg. A:Kirk & Iris
                if ':' in value:
                    section, value = value.split(':')

                    # 'Level 1A'
                    class_name = name + section

                    # Look up the description in the dictionary
                    if class_name in class_desc_dict:
                        name = class_name + ' - ' +  class_desc_dict[class_name]
                    else:
                        name = class_name
                        print('Unknown class type: ' + class_name)
                if value:
                    d.setdefault(time, {})[name] = value

SENDGRID_PASSWORD = environ.get('SENDGRID_PASSWORD')
SENDGRID_USERNAME = environ.get('SENDGRID_USERNAME')

GOOGLE_RECAPTCHA_SECRET_KEY = environ.get('GOOGLE_RECAPTCHA_SECRET_KEY')
CONTACT_EMAIL = 'info@920special.com'
DEBUG_EMAIL = environ.get('DEBUG_EMAIL')
