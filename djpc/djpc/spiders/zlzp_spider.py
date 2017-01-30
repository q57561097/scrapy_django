#coding:utf-8
from scrapy.spider import Spider
from djpc.items import ZwxxItem
from djpc.items import ZlzpItem
from scrapy.selector import Selector
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class MySpider(Spider):
    name = 'dmoz'
    #allowed_domains = ['example.com']
    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python&sm=0&p=1'

    ]

    def parse(self, response):
        sel=Selector(response)
        #item=PcItem()
        #items=[]
        zg=0
        for i in  sel.xpath("//table"):
            item1 = ZwxxItem()
            d= i.xpath(".//td[@class='gzdd']//text()").extract()
            if len(d):
                item1['gzdd']=d[0]
            else:
                item1['gzdd']='无'
            e= i.xpath(".//td[@class='gsmc']//text()").extract()
            if len(e):
                item1['gsmz'] = e[0]

            else:
                item1['gsmz'] = '无'
            de = i.xpath(".//td[@class='zwyx']//text()").extract()
            if len(de):
                item1['zwyx'] = de[0]
            else:
                item1['zwyx'] = '无'
            dh= i.xpath(".//td[@class='zwmc']//a")
            dhh=dh.xpath('string(.)').extract()
            zwurl = dh.xpath("./@href").extract()
            if dhh:
                item1['zwmc'] = dhh[0]

                #if len(zwurl):
                #item1['zwurl']=zwurl[0]
                yield Request(url=zwurl[0], meta={'item_1': item1}, callback=self.sen_parse)
                #else:
                    #item['zwjj'] = '1'
                    #yield item
            else:
                item1['zwmc'] = '无'
                item1['zwjj'] = '2'
                #item['zwurl']='https://www.v2ex.com/t/135918'
                #yield item
            #for fjh in range(1000):
            #yield Request(url=item['zwurl'], meta={'item_1': item}, callback=self.sen_parse)
        nextpag=sel.xpath('//a[@class="next-page"]/@href').extract()
        if nextpag:
            yield Request(url=nextpag[0],  callback=self.parse)
        else:
            yield item1


    def  sen_parse(self,response):
         seld=Selector(response)
         item1=response.meta['item_1']
         item2=ZlzpItem()
         item2['gsmc']=item1['gsmz']
         zwms = seld.xpath("//div[@class='tab-inner-cont']")
         byd=seld.xpath("//h5")
         bydd=byd.xpath('string(.)').extract()

         zwmss = zwms.xpath('string(.)').extract()

         if len(zwmss):
             if len(bydd):
                 item2['gsjj']=zwmss[1].replace(bydd[0],'')
             else:
                 item2['gsjj'] = zwmss[1]

             item1['zwjj']=zwmss[0]
         else:
             item1['zwjj']='3'
             item2['gsjj'] = '无'
         yield item2
         yield item1


