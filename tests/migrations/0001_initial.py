# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("invitations", "0003_auto_20151126_1523"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleSwappableInvitation",
            fields=[
                (
                    "invitation_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="invitations.Invitation",
                    ),
                ),
                ("additonal_field", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=("invitations.invitation",),
        ),
    ]
