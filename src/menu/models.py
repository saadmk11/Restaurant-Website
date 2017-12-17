# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Categories(models.Model):
    cat_name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    cat_img = models.ImageField(
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field"
        )
    height_field = models.IntegerField(
        default=600,
        null=True,
        blank=True,
        )
    width_field = models.IntegerField(
        default=600,
        null=True,
        blank=True,
        )

    def _get_unique_slug(self):
        slug = slugify(self.cat_name)
        unique_slug = slug
        num = 1
        while Categories.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Categories, self).save()

    def __unicode__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse("menu:cat_detail", kwargs={"slug": self.slug})


class Menu(models.Model):
    item = models.CharField(max_length=120, unique=True)
    category = models.ForeignKey(Categories)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    info = models.TextField()
    policy = models.TextField()
    ingredients = models.CharField(max_length=256)
    nutrition = models.CharField(max_length=256)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    img = models.ImageField(
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field"
        )
    height_field = models.IntegerField(
        default=600,
        null=True,
        blank=True,
        )
    width_field = models.IntegerField(
        default=600,
        null=True,
        blank=True,
        )

    class Meta:
        ordering = ["-id"]

    def _get_unique_slug(self):
        slug = slugify(self.item)
        unique_slug = slug
        num = 1
        while Menu.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Menu, self).save()

    def __unicode__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("menu:menu_detail", kwargs={"slug": self.slug})
