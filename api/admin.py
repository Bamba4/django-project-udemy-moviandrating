# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import Movie, Rating

admin.site.register(Movie)
admin.site.register(Rating)