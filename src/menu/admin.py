# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Categories, Menu


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('item',)}
    list_display = ('item', 'category', 'price', 'available', 'featured')
    search_fields = ['item', 'category__cat_name', 'price']
    list_filter = ('available', 'featured', 'category__cat_name')


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_name',)}
    search_fields = ['cat_name']

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Menu, MenuAdmin)
