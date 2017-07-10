# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Categories, Menu
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

def menu_list(request): # shows list of menu items & categories
    query_list = Menu.objects.filter(available=True)
    category = Categories.objects.all()
    query = request.GET.get("q")
    
    if query:
        query_list = query_list.filter(
            Q(item__icontains=query)|
            Q(category__cat_name__icontains=query)
            ).distinct()

    context = { 'query_list': query_list,
                'category': category,
                "title": "Items"
            }

    return render(request, 'menu/menu_list.html', context)

def menu_detail(request, slug=None):
    query = get_object_or_404(Menu, available=True, slug=slug)
    context = { "query": query, }

    return render(request, 'menu/menu_detail.html', context)

def cat_list(request): # shows list of categories
    cat_qs = Categories.objects.all()
    query = request.GET.get("q")

    if query:
        cat_qs = cat_qs.filter(
            Q(cat_name__icontains=query)
            ).distinct()

    context = { "cat_qs": cat_qs,
                "title": "Categories"
                 }

    return render(request, "menu/cat_list.html", context)

def cat_detail(request, cat_name=None): # shows list of items in a category
    categories = get_object_or_404(Categories, cat_name__iexact=cat_name)
    menu_qs = categories.menu_set.filter(available=True)
    query = request.GET.get("q")

    if query:
        menu_qs = menu_qs.filter(
            Q(item__icontains=query)
            ).distinct()

    context = { "menu_qs": menu_qs,
                "title": "Items"

                 }

    return render(request, "menu/cat_detail.html", context)


