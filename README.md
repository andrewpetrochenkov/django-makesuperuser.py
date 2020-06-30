<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-makesuperuser.svg?maxAge=3600)](https://pypi.org/project/django-makesuperuser/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-makesuperuser.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-makesuperuser.py/actions)

### Installation
```bash
$ [sudo] pip install django-makesuperuser
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>