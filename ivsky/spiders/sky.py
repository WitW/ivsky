# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request
from ivsky.items import IvskyItem

class SkySpider(scrapy.Spider):
    name = 'sky'
    start_urls = ['http://ivsky.com/']

    def parse(self, response):

        selector = Selector(response)
        # print(response.text)
        types = selector.xpath("//div[@class='kw']/a")
        for type in types:
            typeUrl = type.xpath("@href").extract()[0]
            typeName = type.xpath("text()").extract()[0]
            # print(typeUrl+" "+typeName)

            yield Request(self.start_urls[0]+typeUrl,callback=self.parseTotalPage,meta={'typeName':typeName})

    def parseTotalPage(self,response):

        typeName = response.meta["typeName"]
        # print(typeName)
        selector = Selector(response)
        # print(response.text)
        pageList = selector.xpath("//div[@class='pagelist']//a//@href").extract()
        for page in pageList:
            yield Request(self.start_urls[0]+page,callback=self.parseGetImg,meta={'typeName':typeName})

    def parseGetImg(self,response):

        typeName = response.meta["typeName"]
        selector = Selector(response)
        imgs = selector.xpath("//div[@class='il_img']//a")
        for img in imgs:
            imgUrl = img.xpath("@href").extract()[0]
            # print(imgUrl+" "+imgName)
            yield Request(self.start_urls[0]+imgUrl,callback=self.parseGetMoreImg)

    def parseGetMoreImg(self,response):
        # / html / body / div[3] / div[4] / ul / li[3] / div / a / img
        selector = Selector(response)
        # print(response.text)
        items = IvskyItem()
        items["imgName"] = response.meta["imgName"]
        items["imgUrl"] = selector.xpath("//div[@class='il_img']//a//img//@src").extract()
        # print(items)
        yield items









