# Generated by Django 3.1.5 on 2021-02-04 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0009_medicalrecord_last_checkup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='last_checkup',
            field=models.DateField(default=datetime.datetime(2021, 2, 4, 4, 30, 56, 892042, tzinfo=utc)),
        ),
    ]