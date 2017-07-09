# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Categories, Menu
from django.shortcuts import render, get_object_or_404

# Create your views here.

def menu_list(request): # shows list of menu items & categories
    query_list = Menu.objects.filter(available=True)
    category = Categories.objects.all()
    context = { 'query_list': query_list,
                'category': category,
            }

    return render(request, 'menu/menu_list.html', context)

def menu_detail(request, slug=None):
    query = get_object_or_404(Menu, available=True, slug=slug)
    context = { "query": query, }

    return render(request, 'menu/menu_detail.html', context)


def cat_list(request): # shows list of categories
    cat_qs = Categories.objects.all()
    context = { "cat_qs": cat_qs, }

    return render(request, "menu/cat_list.html", context)

def cat_detail(request, cat_name=None): # shows list of items in a category
    categories = get_object_or_404(Categories, cat_name__iexact=cat_name)
    menu_qs = categories.menu_set.filter(available=True)
    context = { "menu_qs": menu_qs, }

    return render(request, "menu/cat_detail.html", context)
