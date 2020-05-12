# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-24 01:11
from __future__ import unicode_literals
from django.apps import apps
from django.db import migrations
from django.contrib.auth.models import User


def twl_team(apps, schema_editor):
    User.objects.get_or_create(
        username="TWL Team", email="wikipedialibrary@wikimedia.org"
    )


class Migration(migrations.Migration):

    dependencies = [("users", "0052_auto_20200312_1628")]

    operations = [migrations.RunPython(twl_team, migrations.RunPython.noop)]