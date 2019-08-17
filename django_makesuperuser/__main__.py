#!/usr/bin/env python
"""create/update a superuser with password"""
# -*- coding: utf-8 -*-
import click
import django

"""
export DJANGO_SETTINGS_MODULE=settings
python -m makesuperuser "admin" "password"
python -m makesuperuser "admin" "password" foo@foo.foo
"""

MODULE_NAME = "django_makesuperuser"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s username password [email]' % MODULE_NAME


@click.command()
@click.argument('username')
@click.argument('password')
@click.argument('email',required=False)
def _cli(username,password,email=None):
    django.setup()
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
    except User.DoesNotExist:
        pass

if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
