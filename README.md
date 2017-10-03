# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.11.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment. 

## How to Use

To use this project, follow these steps:

1. Create a directory for your project(`$ mkdir projectname;cd projectname`) 
2. Create your working environment. (`$ python3 -m venv env`)
3. Activate the environment. (`$ source env/bin/activate`)
4. Install Django (`$ pip install django`)
5. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/RadialDevGroup/heroku-django-template/archive/master.zip --name=Procfile projectname .

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``projectname`` with your desired project name.

If you encounter an error like
`CommandError: couldn't download URL https://github.com/RadialDevGroup/heroku-django-template/archive/master.zip to master.zip: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)>`
check out this [StackOverflow](http://stackoverflow.com/questions/41691327/ssl-sslerror-ssl-certificate-verify-failed-certificate-verify-failed-ssl-c)

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
