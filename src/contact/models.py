# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class ContactInfo(models.Model):
    address = models.CharField(max_length=256)
    email = models.EmailField()
    tel = models.CharField(max_length=14)
    fb = models.URLField(max_length=256)
    fb_icon = models.ImageField(
        null=False,
        blank=False,
        height_field="height_field",
        width_field="width_field"
        )
    twitter = models.URLField(max_length=256)
    twitter_icon = models.ImageField(
        null=False,
        blank=False,
        height_field="height_field",
        width_field="width_field"
        )
    instagram = models.URLField(max_length=256)
    instagram_icon = models.ImageField(
        null=False,
        blank=False,
        height_field="height_field",
        width_field="width_field"
        )
    height_field = models.IntegerField(default=30)
    width_field = models.IntegerField(default=30)

    def __unicode__(self):
        return self.email
