```bash

# setup
Install python 3.5

    brew install python3

Install Pip
	Download https://bootstrap.pypa.io/get-pip.py
	python get-pip.py

Install virtualenv
	[sudo] pip install virtualenv

Create a python 3.5 virtualenvironment

    virtualenv 920special

Install python requirements to run the thing

    pip install -r requirements/global.txt -r requirements/dev.txt

####

stuff

setup db

    ./manage.py migrate

Install NPM and Bower for Foundation
	Download NPM https://nodejs.org/en/download/
	[sudo] npm install bower

	npm install
	bower install
```

Finally, run `npm start` to run the Sass compiler. It will re-run every time you save a Sass file.

python manage.py runserver to run it locally

Foundation Docs are http://foundation.zurb.com/sites/docs/