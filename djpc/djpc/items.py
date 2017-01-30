# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys
sys.path.append('/home/zyh/py/mysite')
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from scrapy_djangoitem import DjangoItem, Field

from zlzp.models import Zlzp,Zwxx

class ZlzpItem(DjangoItem):
    django_model = Zlzp
    # define the fields for your item here like:
    # name = scrapy.Field()
class ZwxxItem(DjangoItem):
    django_model = Zwxx
