# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ivsky.items import IvskyItem
import urllib.request
import os

class IvskyPipeline(object):
    def process_item(self, item, spider):
        i=0
        for imgUrl in item["imgUrl"]:
            try:
                path = "photo/"+item["imgName"]+"_"+str(i)+".jpg"
                urllib.request.urlretrieve(imgUrl, path)
                i+=1
            except:
                pass
