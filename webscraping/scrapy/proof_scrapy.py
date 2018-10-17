from scrapy.item import Field
from scrapy.item import Item 
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader


class Pregunta (Item):
    pregunta = Field ()
    id= Field()


class StackOverflowSpider(Spider):
   name = "PrimerSpider"
   start_urls = ['https://stackoverflow.com/']

   def parse(self, response):
       sel = Selector(response)
       preguntas = sel.xpath("//div[@id='question-mini-list']/div/div")

       for i,elem in enumerate(preguntas):
           item = ItemLoader(Pregunta(), elem)
           item.add_xpath('pregunta','//h3/a/text()')
           item.add_value('id',i)
           yield item.load_item()
