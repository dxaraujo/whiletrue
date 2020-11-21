import scrapy
import re

from datetime import date
from whiletrue.items import WhiletrueItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.shell import inspect_response

def process_value(value):
    m = re.search("\#pagina\=([0-9]*)", value)
    if m:
        return '?__vt=lnv:c&pagina=' + m.group(1)

class VivarealSpider(CrawlSpider):

    name = 'vivareal'
    allowed_domains = ['www.vivareal.com.br']
    start_urls = ['https://www.vivareal.com.br/venda/sp/sao-paulo/zona-leste/vila-prudente/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[contains(@title,"Próxima página")]', process_value=process_value), follow=True),
        Rule(LinkExtractor(allow=r'pagina=*'), callback='parse_item'),
    )

    def parse_item(self, response):

        items = response.xpath('//div[contains(@class,"js-card-selector")]//article[contains(@class,"js-property-card")]')

        if items:
            for i, item in enumerate(items):
                path = item.css('a.js-card-title::attr(href)').get()
                url = response.urljoin(path)
                yield scrapy.Request(url=url, callback=self.parse_detail)

        # inspect_response(response, self)
        # nextPage = response.xpath('//a[contains(@title,"Próxima página")]/@data-page').extract_first()
        # if nextPage:
        #     nextUrl = self.base_url_next_page + '?__vt=lnv:c#pagina=' + str(nextPage)
        #     yield scrapy.Request(url=nextUrl, callback=self.parse)
        # yield scrapy.Request(url=response.url, callback=self.parse_detail)

    def parse_detail(self, response):
        
        imovel = WhiletrueItem()

        imovel['url']       = response.url
        imovel['id']        = response.xpath('normalize-space(//span[contains(@class,"js-external-id")]//.)').extract_first()
        imovel['titulo']    = response.xpath('normalize-space(//h1[contains(@class,"js-title-view")]//.)').extract_first()
        imovel['endereco']  = response.xpath('normalize-space(//p[contains(@class,"js-address")]//.)').extract_first()

        pattern = re.compile(r"lat: '(.*)',")
        imovel['lat']       = response.xpath('//script[contains(.,"lat:")]/text()').re(pattern)[0]

        pattern = re.compile(r"lon: '(.*)',")
        imovel['lon']       = response.xpath('//script[contains(.,"lon:")]/text()').re(pattern)[0]

        imovel['data']      = str(date.today())

        preco               = response.xpath('normalize-space(//h3[contains(@class,"js-price-sale")])').re("R\$ (.*)")
        preco               = (preco and preco[0]) or 0
        if preco != 0:
            imovel['preco'] = int(re.sub('[^0-9]', '', preco))
        else:
            imovel['preco'] = preco

        condominio          = response.xpath('normalize-space(//span[contains(@class,"js-condominium")])').re("R\$ (.*)")
        condominio          = (condominio and condominio[0]) or 0
        if condominio != 0:
            imovel['condominio'] = int(re.sub('[^0-9]', '', condominio))
        else:
            imovel['condominio'] = condominio
   
        iptu                = response.xpath('normalize-space(//span[contains(@class,"js-condominium")])').re("R\$ (.*)")
        iptu                = (iptu and iptu[0]) or 0
        if iptu != 0:
            imovel['iptu']  = int(re.sub('[^0-9]', '', iptu))
        else:
            imovel['iptu']  = iptu

        imovel['area']      = response.xpath('normalize-space(.//li[contains(@class, "js-area")]//span/text())').extract_first()
        imovel['quartos']   = response.xpath('normalize-space(.//li[contains(@class, "js-bedrooms")]//span/text())').extract_first()
        imovel['banheiros'] = response.xpath('normalize-space(.//li[contains(@class, "js-bathrooms")]//span/text())').extract_first()
        suites              = response.xpath('normalize-space(.//li[contains(@class, "js-bathrooms")]//small/text())').extract_first()
        if suites:
            imovel['suites']    = int(re.sub('[^0-9]', '', suites))
        imovel['vagas']     = response.xpath('normalize-space(.//li[contains(@class, "js-parking")]//span/text())').extract_first()
        imovel['descricao'] = response.xpath('normalize-space(.//div[contains(@class, "description__body")]//p[contains(@class, "description__text")]/text())').extract_first()

        yield imovel