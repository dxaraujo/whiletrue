import scrapy
import random

from whiletrue.items import WhiletrueItem

class VivarealSpider(scrapy.Spider):

    name = 'vivareal'
    allowed_domains = ['www.vivareal.com.br']
    start_urls = ['https://www.vivareal.com.br/venda/ceara/fortaleza/?__vt=lnv:c']
    base_url = 'https://www.vivareal.com.br/venda'

    def parse(self, response):

        items = response.xpath('//div[contains(@class,"js-card-selector")]//article[contains(@class,"js-property-card")]')

        if items:

            for i, item in enumerate(items):

                path = item.css('a.js-card-title::attr(href)').get()
                url = self.base_url + path + '?__vt=lnv:c'
                yield scrapy.Request(url=url, callback=self.parse_detail)

        nextPage = response.css('a.js-change-page::attr(data-page)').getall()[-1]

        if nextPage:

            nextUrl = self.base_url + '?__vt=lnv:c#pagina=' + str(nextPage)
            yield scrapy.Request(url=nextUrl, callback=self.parse)

    def parse_detail(self, response):
        
        imovel = WhiletrueItem()

        imovel['url']       = response.url
        imovel['titulo']    = response.xpath('normalize-space(//h1[contains(@class,"js-title-view")]//.)').extract_first()

        # data                = response.xpath('normalize-space(//div[contains(@class,"OLXad-date")]//p)').re("Inserido em: (\d*) (\w*)")
        # imovel['data']      = date(date.today().year, self.converteMes[data[1]], int(data[0]))

        # preco               = response.xpath('normalize-space(//span[contains(@class,"actual-price")])').re("R\$ (.*)")
        # preco               = (preco and preco[0]) or 0
        # if preco != 0:
        #     imovel['preco']     = int(re.sub('[^0-9]', '', preco))
        # else:
        #     imovel['preco']     = preco


        # imovel['descricao'] = response.xpath('normalize-space(//div[contains(@class,"OLXad-description")]//p)').extract_first()

        # detalhes = response.xpath('//div[contains(@class, "OLXad-details")]//li[contains(@class, "item")]')

        # atributo = None
        # valor    = None
        # for i, detalhe in enumerate(detalhes):
        #     atributo = detalhe.xpath('normalize-space(.//span[contains(@class, "term")]/text())').extract_first()
        #     valor    = detalhe.xpath('normalize-space(.//strong[contains(@class, "description")]/text())').extract_first()
            
        #     if (atributo == 'Tipo:'):
        #         imovel['tipo'] = valor
        #     elif (atributo == 'Área útil:'):
        #         area = int(re.sub('[^0-9]', '', valor))
        #         imovel['area_util'] = area
        #     elif (atributo == 'Área construída:'):
        #         area = int(re.sub('[^0-9]', '', valor))
        #         imovel['area_construida'] = area
        #     elif (atributo == 'Quartos:'):
        #         imovel['n_quartos'] = valor
        #     elif (atributo == 'Vagas na garagem:'):
        #         imovel['vagas_garagem'] = valor
        #     elif (atributo == 'Condomínio:'):
        #         imovel['condominio'] = valor

        # localizacao = response.xpath('//div[contains(@class, "OLXad-location")]//li[contains(@class, "item")]')

        # atributo = None
        # valor    = None
        # for i, loc in enumerate(localizacao):
        #     atributo = loc.xpath('normalize-space(.//span[contains(@class, "term")]/text())').extract_first()
        #     valor    = loc.xpath('normalize-space(.//strong[contains(@class, "description")]/text())').extract_first()
            
        #     if (atributo == 'Município:'):
        #         imovel['municipio'] = valor
        #     elif (atributo == 'CEP do imóvel:'):
        #         imovel['cep'] = valor
        #     elif (atributo == 'Bairro:'):
        #         imovel['bairro'] = valor
            
        # imovel['id'] = response.xpath('normalize-space(//span[contains(@class, "js-external-id")]//.)').extract_first()

        yield imovel