# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_auto_20160929_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
