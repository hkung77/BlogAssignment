# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogposts_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogposts',
            name='Image_link',
        ),
    ]
