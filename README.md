# Heroku Django Starter Template

An utterly fantastic project starter template for Django 2.2.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.7 runtime environment.

## How to Use

### Prerequisites

 - [Python 3.7](https://www.python.org/downloads/) should be installed on your machine
 - [Pipenv](https://docs.pipenv.org/en/latest/) (`pip install pipenv`)

### Option 1: One-command script

Try the [Cheat Script](https://github.com/RadialDevGroup/heroku-django-template/wiki/Cheat-Script-(django_new))

### Option 2: Manual steps

1. Create a directory for your project(`$ mkdir projectname;cd projectname`)
2. Activate the environment. (`$ pipenv shell`)
3. Install Django (`$ pipenv install django~=2.2`)
4. Remove the Pipfile to allow the template to replace it. (`$ rm Pipfile`)
5. Create a new project using this template:
    ```
    $ django-admin.py startproject --template=https://github.com/RadialDevGroup/heroku-django-template/archive/Django-2.2.zip --name=Procfile --name settings.yml --name settings.yml.example projectname .
    ```

    (If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

    You can replace ``projectname`` with your desired project name.

6. Install dependencies. (`pipenv install --dev`)

## Troubleshooting
  - If you encounter an error like
      
      `CommandError: couldn't download URL https://github.com/RadialDevGroup/heroku-django-template/archive/Django-2.2.zip to Django-2.2.zip: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)>`
      
      check out this [StackOverflow](http://stackoverflow.com/questions/41691327/ssl-sslerror-ssl-certificate-verify-failed-certificate-verify-failed-ssl-c)

  - If pipenv install fails due to a `library not found for -lssl`, [try this](https://stackoverflow.com/a/39800677).

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
