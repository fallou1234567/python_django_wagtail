from django.db import models
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.models import Page
from django.template.response import TemplateResponse


class HomePage(Page):
    #pass
    template = 'page/homePage.html'

