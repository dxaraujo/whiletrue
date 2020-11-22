import scrapy
import json

from whiletrue.items import ZapItem

class ZapSpider(scrapy.Spider):

    name = 'zap'
    allowed_domains = ['glue-api.zapimoveis.com.br']
    link = 'https://glue-api.zapimoveis.com.br/v2/listings?0=U&1=n&2=i&3=t&4=T&5=y&6=p&7=e&8=_&9=N&10=O&11=N&12=E&categoryPage=RESULT&business=SALE&listingType=USED&portal=ZAP&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=0&developmentsSize=0&superPremiumSize=0&addressCountry=&addressState=São Paulo&addressCity=&addressZone=&addressNeighborhood=&addressStreet=&addressAccounts=&addressType=city&addressLocationId=BR>Sao Paulo&addressPointLat=&addressPointLon=&__zt=lva:c,rnk_gz:rescore_ctr_model&size={0}&from={1}&page={2}'
    domain = 'www.zapimoveis.com.br'
    start_urls = []

    size = 300
    for i in range(0, 1000):
        start_urls.append(link.format(size, i * size, i + 1))

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        listings = jsonresponse['search']['result']['listings']
        for listing in listings:
            item = ZapItem()

            item['createdAt'] = listing['listing'].get('createdAt', '')
            item['title'] = listing['listing'].get('title', '')
            item['description'] = listing['listing'].get('description', '')

            item['businessType'] = ''
            item['monthlyCondoFee'] = ''
            item['price'] = ''
            item['yearlyIptu'] = ''
            pricingInfos = listing['listing'].get('pricingInfos', '')
            if pricingInfos:
                if len(pricingInfos) > 0:
                    item['businessType'] = pricingInfos[0].get('businessType', '')
                    item['monthlyCondoFee'] = pricingInfos[0].get('monthlyCondoFee', '')
                    item['price'] = pricingInfos[0].get('price', '')
                    item['yearlyIptu'] = pricingInfos[0].get('yearlyIptu', '')

            item['country'] = listing['listing']['address'].get('country', '')
            item['state'] = listing['listing']['address'].get('state', '')
            item['stateAcronym'] = listing['listing']['address'].get('stateAcronym', '')
            item['city'] = listing['listing']['address'].get('city', '')
            item['zipCode'] = listing['listing']['address'].get('zipCode', '')
            item['complement'] = listing['listing']['address'].get('complement', '')

            item['latitude'] = 0
            item['longitude'] = 0
            point = listing['listing']['address'].get('point', '')
            if point:
                item['latitude'] = point['lat']
                item['longitude'] = point['lon']

            item['level'] = listing['listing']['address'].get('level', '')
            item['street'] = listing['listing']['address'].get('street', '')
            item['streetNumber'] = listing['listing']['address'].get('streetNumber', '')

            item['bathrooms'] = ''
            bathrooms = listing['listing'].get('bathrooms', '')
            if bathrooms:
                if len(bathrooms) > 0:
                    item['bathrooms'] = bathrooms[0]

            item['bedrooms'] = ''
            bedrooms = listing['listing'].get('bedrooms', '')
            if bedrooms:
                if len(bedrooms) > 0:
                    item['bedrooms'] = bedrooms[0]

            item['listingType'] = listing['listing'].get('listingType', '')

            item['parkingSpaces'] = ''
            parkingSpaces = listing['listing'].get('parkingSpaces', '')
            if parkingSpaces:
                if len(parkingSpaces) > 0:
                    item['parkingSpaces'] = parkingSpaces[0]

            item['suites'] = ''
            suites = listing['listing'].get('suites', '')
            if suites:
                if len(suites) > 0:
                    item['suites'] = suites[0]

            item['totalAreas'] = ''
            totalAreas = listing['listing'].get('totalAreas', '')
            if totalAreas:
                if len(totalAreas) > 0:
                    item['totalAreas'] = totalAreas[0]

            item['usableAreas'] = ''
            usableAreas = listing['listing'].get('usableAreas', '')
            if usableAreas:
                if len(usableAreas) > 0:
                    item['usableAreas'] = usableAreas[0]

            item['usageTypes'] = ''
            usageTypes = listing['listing'].get('usageTypes', '')
            if usageTypes:
                if len(usageTypes) > 0:
                    item['usageTypes'] = usageTypes[0]

            item['image'] = ''
            media = listing.get('media', '')
            if media:
                if len(media) > 0:
                    item['image'] = media[0]['url']

            href = listing['link'].get('href', '')
            item['url'] = self.domain + href
            yield item
        pass
