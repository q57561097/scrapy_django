# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from zlzp.models import Zwxx,Zlzp

class DjpcPipeline(object):
    def process_item(self, item2, spider):
        item2.save()


        return item2
class DjpcPipeline1(object):
    def process_item(self, item1, spider):
        r1=Zlzp.objects.get(gsmc=item1['gsmz'])
        item1.save()
        r2=Zwxx.objects.get(gsmz=item1['gsmz'],zwmc=item1['zwmc'])
        r2.gsmcc.add(r1)
        r2.save()
        return item1
