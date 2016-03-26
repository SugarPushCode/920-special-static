# -*- coding: utf-8 -*-

from __future__ import absolute_import

from collections import namedtuple

_Person = namedtuple('Person', 'slug,name')


class Person(_Person):

    @property
    def img(self):
        return '/static/img/people/{}.jpg'.format(self.slug)


TEACHER = 'teacher'
DJ = 'dj'

people = (
    Person(name='Iris Tarou', slug='iristarou',),
    Person(name='Kirk Tarou', slug='kirktarou',),
    Person(name='Manu Smith', slug='manusmith',),
    Person(name='Ann Mony', slug='annmony',),
    Person(name='Nicole Zuckerman', slug='nicolezuckerman',),
    Person(name='Shannon Lea Watkins', slug='shannonleawatkins',),
    Person(name='Jessica Boddicker', slug='jessicaboddicker',),
    Person(name='Ellen Huffman', slug='ellenhuffman',),
    Person(name='Julia Farrell', slug='juliafarrel',),
    Person(name='Jessica King', slug='jessking',),
    Person(name='Jean Palamountain', slug='jeanpalamountain',),
    Person(name='Ryan Calloway', slug='ryancalloway',),
    Person(name='Carl Nelson', slug='carlnelson',),
    Person(name='Douglas Matthews', slug='douglasmatthews',),
    Person(name='Zain Memoin', slug='zainmemoin',),
    Person(name='Bromley Palamountain', slug='bromleypalamountain',),
    Person(name='Kevin Weng', slug='kevinweng',),
    Person(name='Allen Kerr', slug='allenkerr',),
    Person(name='Alex Fernandez', slug='alexfernandez',),
    Person(name='Dhruv Bhargava', slug='dhruvbarghava',),
    Person(name='Nathan Dias', slug='nathandias',),
    Person(name='Hep Jen', slug='hepjen',),
    Person(name='Arnold Cabreza', slug='arnoldcabreza',),
    Person(name='Nirav Sanghani', slug='niravsanghani',),
    Person(name='Ben Nathan', slug='bennathan',),
)

teachers = (
    'iristarou',
    'kirktarou',
    'manusmith',
    'annmony',
    'nicolezuckerman',
    'shannonleawatkins',
    'jessicaboddicker',
    'ellenhuffman',
    'juliafarrel',
    'jessking',
    'jeanpalamountain',
    'ryancalloway',
    'carlnelson',
    'douglasmatthews',
    'zainmemoin',
    'bromleypalamountain',
    'kevinweng',
)

djs = (
    'allenkerr',
    'manusmith',
    'nicolezuckerman',
    'alexfernandez',
    'dhruvbarghava',
    'nathandias',
    'hepjen',
    'arnoldcabreza',
    'niravsanghani',
    'bennathan',
)


PEOPLE = {person.slug: person for person in people}

TEACHERS = map(PEOPLE.get, teachers)
DJS = map(PEOPLE.get, djs)

DJ1 = 'allenkerr'
DJ2 = 'alexfernandez'

THIS_WEEK = {
    'dj1': PEOPLE[DJ1],
    'dj2': PEOPLE[DJ2],
}
