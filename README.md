# installation instructions

configure the virtualenv
- pip install pipenv
- pipenv --python 3.10
- pipenv install


enter virtualenv
- pipenv shell

build the database
- python manage.py migrate

run the server
- python manage.py runserver
