<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-makesuperuser.svg?longCache=True)](https://pypi.org/project/django-makesuperuser/)
[![](https://img.shields.io/pypi/v/django-makesuperuser.svg?maxAge=3600)](https://pypi.org/project/django-makesuperuser/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/django-makesuperuser.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/django-makesuperuser.py/)

#### Installation
```bash
$ [sudo] pip install django-makesuperuser
```

#### `settings.py`
```python
if DEBUG:
    INSTALLED_APPS+= ["django_makesuperuser"]
```

#### Commands
command|`help`
-|-
`python manage.py makesuperuser` |create/update a superuser with password

#### Examples
```bash
$ python manage.py makesuperuser --username admin --password admin
$ python manage.py makesuperuser --username admin --password admin --email 'admin@example.com'
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>