# Generated by Django 4.2.7 on 2024-08-02 07:55
import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_executivemember_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="executivemember",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 2, 7, 52, 20, 210123, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date Joined",
            ),
        ),
    ]
