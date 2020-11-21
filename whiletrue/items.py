# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WhiletrueItem(scrapy.Item):
    id              = scrapy.Field()
    titulo          = scrapy.Field()
    endereco        = scrapy.Field()
    lat             = scrapy.Field()
    lon             = scrapy.Field()
    data            = scrapy.Field()
    preco           = scrapy.Field()
    condominio      = scrapy.Field()
    iptu            = scrapy.Field()
    area            = scrapy.Field()
    quartos         = scrapy.Field()
    banheiros       = scrapy.Field()
    suites          = scrapy.Field()
    vagas           = scrapy.Field()
    descricao       = scrapy.Field()
    url             = scrapy.Field()