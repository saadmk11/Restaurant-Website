# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Categories, Menu


def menu_list(request):  # shows list of menu items & categories
    query_list = Menu.objects.filter(available=True)
    category = Categories.objects.all()
    query = request.GET.get("q")
    if query:
        query_list = query_list.filter(
            Q(item__icontains=query) |
            Q(category__cat_name__icontains=query)
            ).distinct()

    paginator = Paginator(query_list, 12)
    page = request.GET.get("page")
    try:
        query_l = paginator.page(page)
    except PageNotAnInteger:
        query_l = paginator.page(1)
    except EmptyPage:
        query_l = paginator.page(paginator.num_pages)

    context = {"query_l": query_l,
               "category": category,
               "title": "Items"
               }
    return render(request, 'menu/menu_list.html', context)


def menu_detail(request, slug=None):
    query = get_object_or_404(Menu, available=True, slug=slug)
    recommended = Menu.objects.filter(
        available=True,
        category=query.category
        ).order_by("?")[:4]

    context = {"query": query,
               "recommended": recommended,
               }
    return render(request, 'menu/menu_detail.html', context)


def cat_list(request):  # shows list of categories
    cat_qs = Categories.objects.all()

    query = request.GET.get("q")
    if query:
        cat_qs = cat_qs.filter(
            Q(cat_name__icontains=query)
            ).distinct()

    paginator = Paginator(cat_qs, 12)
    page = request.GET.get("page")
    try:
        query_l = paginator.page(page)
    except PageNotAnInteger:
        query_l = paginator.page(1)
    except EmptyPage:
        query_l = paginator.page(paginator.num_pages)

    context = {"query_l": query_l,
               "title": "Categories"
               }
    return render(request, "menu/cat_list.html", context)


def cat_detail(request, slug=None):  # shows list of items in a category
    categories = get_object_or_404(Categories, slug=slug)
    menu_qs = categories.menu_set.filter(available=True)

    query = request.GET.get("q")
    if query:
        menu_qs = menu_qs.filter(
            Q(item__icontains=query)
            ).distinct()

    paginator = Paginator(menu_qs, 12)
    page = request.GET.get("page")
    try:
        query_l = paginator.page(page)
    except PageNotAnInteger:
        query_l = paginator.page(1)
    except EmptyPage:
        query_l = paginator.page(paginator.num_pages)

    context = {"query_l": query_l,
               "title": "Items",
               "categories": categories,
               }
    return render(request, "menu/cat_detail.html", context)
