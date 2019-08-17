<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-makesuperuser.svg?longCache=True)](https://pypi.org/project/django-makesuperuser/)
[![](https://img.shields.io/pypi/v/django-makesuperuser.svg?maxAge=3600)](https://pypi.org/project/django-makesuperuser/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-makesuperuser.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-makesuperuser.py/)

#### Installation
```bash
$ [sudo] pip install django-makesuperuser
```

#### Commands
command|`help`
-|-
`python manage.py makesuperuser` |create/update a superuser with password

#### Executable modules
usage|`__doc__`
-|-
`python -m django_makesuperuser username password [email]` |create/update a superuser with password

#### Examples
example#1 - management command:

`settings.py`
```python
INSTALLED_APPS+= ["django_makesuperuser"]
```

```bash
$ python manage.py makesuperuser --username admin --password admin
$ python manage.py makesuperuser --username admin --password admin --email foo@foo.foo
```

example#2 - python module cli:
```bash
$ export DJANGO_SETTINGS_MODULE=settings
$ python -m django_makesuperuser "username" "password"
$ python -m django_makesuperuser "username" "password" foo@foo.foo
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>