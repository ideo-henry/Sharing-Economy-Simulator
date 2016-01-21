# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0003_sharing'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sharing',
            field=models.BooleanField(default=False),
        ),
    ]
