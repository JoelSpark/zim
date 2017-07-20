## Host Setup

### Dependencies
* python modules: `sudo pip install virtualenv autoenv`
* heroku cli: `wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh`
* database: `sudo apt-get install libpq-dev postgresql postgresql-contrib`

### Host Configuration
* autoenv: `echo "source `which activate.sh`" >> ~/.bashrc`

## Project Setup

### Environment Stuffs
* `django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile  NAME`
* `cd NAME`
* Create git repo: `git init`
* Create virtual environment: `virtualenv env`
* Set up autoenv file:
```
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
```
* Modify .gitignore (remove `.env`, add `env/`)
* Add git remotes

### Heroku Stuffs

* Set up Procfile: `web: gunicorn app:app`
* Set up runtime.txt: `python-2.7.12`
* `heroku git:remote -a zim-stage -r stage`

### Dependencies

* `pip install django gunicorn dj_database_url whitenoise psycopg2`

### Database

* `sudo su - postgres
* `psql`
* `CREATE DATABASE name;`
* `CREATE USER <name> WITH PASSWORD '<password>';``
* Configure user:
```
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

* Grant privileges: `GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`
```
* Update database settings:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
* Set up first migrations:
```
python manage.py makemigrations
python manage.py migrate
```
* Create superuser: `python manage.py createsuperuser`

## Refresher Notes:

* `pip freeze > requirements.txt` to capture modules for use in virtual environment FROM WITHIN the virtualenv
* `heroku run <command>`
* `python manage.py migrate`
