# Generated by Django 4.1 on 2022-08-09 18:19

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", accounts.models.CustomUserManager()),
            ],
        ),
    ]
