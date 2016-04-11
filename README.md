# Setup

There are two options for running it, 1) via docker, or 2) via django. The first method only requires docker to be installed and is much simpler for most users, while the second version is more flexible and better for advanced users.

### Method 1: Docker

First follow the getting started instructions at [docker.com](https://docs.docker.com), or install via [homebrew](http://brew.sh). Make sure that you have docker and docker-compose installed, I recommend installing them via docker-toolbox which gives you everything you need that is docker related.

Next, simply run

    docker-compose up

### Method 2: django and `manage.py`

If you know how to use npm and python virtual environments then this section is for you! If you don't then you'll need to talk to one of the devs that does as documenting the instalation of python, node, virtualenv, and other build tools is out of the scope of this doc.

1. ensure python3 and pip are installed
2. create a virtual environment with ```--python=`which pyton3` ```
    something like this: `mkvirtualenv 920-special-static --python /usr/local/bin/python3.5`
3. ensure node.js and npm are installed
4. `make bootstrap`, this will
    - clear the static, node, and bower dirs
    - install all node dependencies like bower and foundation
    - install all python requirements

Using the django entrypoint of `mangage.py` we can do many things.

Like run the server! When running in debug mode django will automatically compile static assets on each request so changes will be reflected immeadately.

    DEBUG=1 ./manage.py runserver

> Note: This project uses environment variables to set several things, so the `DEBUG=1` is critical here.

To see what the static assets will be in production use collectstatic. This command will clear the `./static` dir and regenerate it with all the static assets in the django project.

    DEBUG=1 ./manage.py collectstatic --clear --no-input

> If you see an error like `File to import not found or unreadable: util/util` check that you have run `npm install`

# Project organization

This project is using a standard django organization (which might be odd for people used to other systems).
This means that as much as possible is being done with python via django. This includes:

- templates
- scss compilation
- static asset collection
- development server

```
.
├── Dockerfile                  # docker deffinition
├── docker-compose.yml          # docker compose deffinition
├── ISSUE_TEMPLATE              # git-hub template for new issues
├── Makefile                    # bootstrap for local development
├── Procfile                    # heroku worker deffinitions
├── README.md                   # this file!
├── app.json                    # heroku app deffinition
├── bower.json                  # asset management for foundation
├── config
│   ├── nginx.conf.erb
│   └── uwsgi.ini
├── data.yml                    # hack database until we setup a real one
├── entrypoint.sh               # heroku and docker entrypoint script
├── lindy                       # django and python code
│   ├── db.sqlite3              # temp database for local dev, never check in
│   ├── special920              # config for the django app
│   │   ├── settings.py         # django main config
│   │   ├── urls.py             # django main urls
│   │   └── wsgi.py             # wsgi app for nginx/uwsgi
│   └── static920               # django app for the 920 site
│       ├── models              # data models for 920
│       ├── static
│       │   ├── img
│       │   ├── js
│       │   └── scss
│       │       ├── _*.scss     # imported into app.scss
│       │       ├── app.scss    # main entrypoint for sass
│       │       └── fonts       # fonts for stuff
│       ├── templates           # django templates using jinja
│       ├── urls.py
│       └── views.py            # django main views
├── manage.py                   # django entrypoint for commands
├── package.json                # node deffinition
├── pngs                        # redundant images?
├── requirements.txt            # python requirements
├── setup.cfg                   # python setup.cfg
└── wsgi.py                     # unused?
```
