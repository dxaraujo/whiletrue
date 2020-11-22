# Define here the models for your scraped items
#
# See documentation in:
# https://docs.org/en/latest/topics/items.html

from scrapy import Item, Field

class WhiletrueItem(Item):
    id              = Field()
    titulo          = Field()
    endereco        = Field()
    lat             = Field()
    lon             = Field()
    data            = Field()
    preco           = Field()
    condominio      = Field()
    iptu            = Field()
    area            = Field()
    quartos         = Field()
    banheiros       = Field()
    suites          = Field()
    vagas           = Field()
    descricao       = Field()
    url             = Field()

class ZapItem(Item):
    id              = Field()
    createdAt       = Field()
    title           = Field()
    description     = Field()
    businessType    = Field()
    listingType     = Field()
    country         = Field()
    state           = Field()
    stateAcronym    = Field()
    city            = Field()
    zipCode         = Field()
    level           = Field()
    street          = Field()
    streetNumber    = Field()
    complement      = Field()
    latitude        = Field()
    longitude       = Field()
    bathrooms       = Field()
    bedrooms        = Field()
    suites          = Field()
    parkingSpaces   = Field()
    monthlyCondoFee = Field()
    yearlyIptu      = Field()
    price           = Field()
    totalAreas      = Field()
    usableAreas     = Field()
    usageTypes      = Field()
    url             = Field()
