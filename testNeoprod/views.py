from http.client import HTTPResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.shortcuts import render

from wagtail.models import Page
from wagtail.search.models import Query


def profile(request):
    return render(request,'page/profile.html')

def feed(request):
    return render(request,'page/feed.html')

def detail(request):
    return render(request,'page/detail.html')

def acceuil(request):
    return render(request,'page/acceuil.html')
