# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categories, Menu
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('item',)}


admin.site.register(Categories)
admin.site.register(Menu, MenuAdmin)