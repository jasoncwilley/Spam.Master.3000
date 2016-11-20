# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0011_auto_20160930_1444'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweet',
            new_name='Spam',
        ),
        migrations.RenameField(
            model_name='spam',
            old_name='tweet_text',
            new_name='text',
        ),
    ]
