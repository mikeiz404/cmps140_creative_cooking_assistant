# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.xlib.pydispatch import dispatcher
from scrapy.core import signals
from scrapy.core.exceptions import DropItem
from scraper import items
import re
        
class DropPipeline(object):
    """
    Drops invalid items.
    """
    def process_item(self, domain, item):
        print "PARENT: ", type(item.parent)
        print "NAME: ", type(item.name)
        if item.parent == None or item.name == None or item.parent == '' or item.name == '':
            raise DropItem("Item has no parent or name.")
        else:
            return item
            
class SanitizePipeline(object):
    """
    Cleans up the text in the item fields.
    """
    def process_item(self, domain, item):
        print "CLEAN: ", item
        if item.parent == None: raise DropItem("Item has no parent or name.")
        def clean(string):
            re.escape(item.parent.lower())
            
        item.parent = clean(item.parent)
        item.name = clean(item.name)
        return item
        
class ExportPipeline(object):
    """
    Writes items out to file.
    """
    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        
    def spider_opened(self, spider):
        self.files={items.IngredientItem: open('ingredients.txt','wa')}
        
    def process_item(self, domain, item):
        line = "(%s,%s)\n" % (item.parent, item.name)
        self.files[type(item)].writelines([line])
        return item
            
    def spider_closed(self, spider):
        for afile in self.files.values():
            afile.close()
