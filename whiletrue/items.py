# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WhiletrueItem(scrapy.Item):
    id              = scrapy.Field()
    data            = scrapy.Field()
    titulo          = scrapy.Field()
    preco           = scrapy.Field()
    condominio      = scrapy.Field()
    iptu            = scrapy.Field()
    tipo            = scrapy.Field()
    area            = scrapy.Field()
    n_quartos       = scrapy.Field()
    n_banheiros     = scrapy.Field()
    vagas_garagem   = scrapy.Field()
    bairro          = scrapy.Field()
    municipio       = scrapy.Field()
    cep             = scrapy.Field()
    descricao       = scrapy.Field()
    url             = scrapy.Field()