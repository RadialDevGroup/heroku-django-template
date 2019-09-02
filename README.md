# Heroku Django Starter Template

An utterly fantastic project starter template for Django 2.2.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.7 runtime environment.

## How to Use

To use this project, follow these steps:

1. Create a directory for your project(`$ mkdir projectname;cd projectname`)
2. Activate the environment. (`$ pipenv shell`)
3. Install Django (`$ pipenv install django~=2.2`)
4. Create a new project using this template

    $ django-admin.py startproject --template=https://github.com/RadialDevGroup/heroku-django-template/archive/Django-2.2.zip --name=Procfile projectname .

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


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
