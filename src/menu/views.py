# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Categories, Menu
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

def menu_list(request): # shows list of menu items & categories
    query_list = Menu.objects.filter(available=True).order_by("-id")
    category = Categories.objects.all().order_by("-id")
    
    paginator = Paginator(query_list, 16)
    page = request.GET.get("page")
    try:
        query_l = paginator.page(page)
    except PageNotAnInteger:
        query_l = paginator.page(1)
    except EmptyPage:
        query_l = paginator.page(paginator.num_pages)

    query = request.GET.get("q")   
    if query:
        query_list = query_list.filter(
            Q(item__icontains=query)|
            Q(category__cat_name__icontains=query)
            ).distinct()

    context = { 'query_list': query_list,
                "query_l": query_l,
                'category': category,
                "title": "Items"
            }

    return render(request, 'menu/menu_list.html', context)


def menu_detail(request, slug=None):
    query = get_object_or_404(Menu, available=True, slug=slug)
    context = { "query": query, }

    return render(request, 'menu/menu_detail.html', context)


def cat_list(request): # shows list of categories
    cat_qs = Categories.objects.all().order_by("-id")

    paginator = Paginator(cat_qs, 16)
    page = request.GET.get("page")
    try:
        query_l = paginator.page(page)
    except PageNotAnInteger:
        query_l = paginator.page(1)
    except EmptyPage:
        query_l = paginator.page(paginator.num_pages)

    query = request.GET.get("q")
    if query:
        cat_qs = cat_qs.filter(
            Q(cat_name__icontains=query)
            ).distinct()

    context = { "cat_qs": cat_qs,
                "query_l": query_l,
                "title": "Categories"
                 }

    return render(request, "menu/cat_list.html", context)


def cat_detail(request, cat_name=None): # shows list of items in a category
    categories = get_object_or_404(Categories, cat_name__iexact=cat_name)
    menu_qs = categories.menu_set.filter(available=True)

    paginator = Paginator(menu_qs, 16)
    page = request.GET.get("page")
    try:
        query_l = paginator.page(page)
    except PageNotAnInteger:
        query_l = paginator.page(1)
    except EmptyPage:
        query_l = paginator.page(paginator.num_pages)

    query = request.GET.get("q")
    if query:
        menu_qs = menu_qs.filter(
            Q(item__icontains=query)
            ).distinct()

    context = { "menu_qs": menu_qs,
                "query_l": query_l,
                "title": "Items"

                 }

    return render(request, "menu/cat_detail.html", context)


