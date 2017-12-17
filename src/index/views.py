# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from menu.models import Categories, Menu


def home(request):
    queryset = Menu.objects.filter(
        available=True,
        featured=True
        ).order_by("?")[:4]
    return render(request, "index/home.html", {"queryset": queryset})


def about(request):
    return render(request, "index/about.html", {})
