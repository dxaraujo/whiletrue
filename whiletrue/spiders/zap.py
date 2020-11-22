import scrapy
import json

class ZapSpider(scrapy.Spider):

    name = 'zap'
    allowed_domains = ['glue-api.zapimoveis.com.br']
    # link = 'https://glue-api.zapimoveis.com.br/v2/listings?0=U&1=n&2=i&3=t&4=T&5=y&6=p&7=e&8=_&9=N&10=O&11=N&12=E&categoryPage=RESULT&business=SALE&listingType=USED&parentId=null&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=1&developmentsSize=3&superPremiumSize=3&addressCountry=&addressState=&addressCity=&addressZone=&addressNeighborhood=&addressStreet=&addressAccounts=&addressType=&addressLocationId=&addressPointLat=&addressPointLon=&__zt=lva:c,rnk_gz:rescore_ctr_default&size=24&from={0}&page={1}'
    link = 'https://glue-api.zapimoveis.com.br/v2/listings?business=SALE&categoryPage=RESULT&parentId=null&listingType=USED&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=1&developmentsSize=3&superPremiumSize=3&addressCountry=&addressState=S%C3%A3o+Paulo&addressCity=S%C3%A3o+Paulo&addressZone=Zona+Leste&addressNeighborhood=Vila+Prudente&addressStreet=&addressAccounts=&addressType=neighborhood&addressLocationId=BR%3ESao+Paulo%3ENULL%3ESao+Paulo%3EZona+Leste%3EVila+Prudente&addressPointLat=-23.579014&addressPointLon=-46.579756&__zt=lva:c,rnk_gz:rescore_ctr_default&size=24&from={0}&page={1}'
    start_urls = []

    size = 24
    for i in range(1,40):
        start_urls.append(link.format((i - 1) * size, i))

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        listings = jsonresponse['search']['result']['listings']
        for listing in listings:
            self.parse_listing(listing)
        pass

    def parse_listing(self, response):

        item = ZapItem()

        item['createdAt'] = response['createdAt'],
        item['title'] = response['title'],
        item['description'] = response['description'],
        item['businessType'] = response['pricingInfos']['businessType'],
        item['country'] = response['address']['country'],
        item['state'] = response['address']['state'],
        item['stateAcronym'] = response['address']['stateAcronym'],
        item['city'] = response['address']['city'],
        item['zipCode'] = response['address']['zipCode'],
        item['complement'] = response['address']['complement'],

        point = response['address']['point']
        if point:
            item['latitude'] = point['lat']
            item['longitude'] = response['lon']

        item['level'] = response['address']['level'],
        item['street'] = response['address']['street'],
        item['streetNumber'] = response['address']['streetNumber'],

        item['bathrooms'] = response['bathrooms'][0],
        item['bedrooms'] = response['bedrooms'][0],
        # buildings
        item['listingType'] = response['listingType'],
        item['parkingSpaces'] = response['parkingSpaces'][0],

        item['monthlyCondoFee'] = response['pricingInfos']['monthlyCondoFee'],
        item['price'] = response['pricingInfos']['price'],
        item['yearlyIptu'] = response['pricingInfos']['yearlyIptu'],

        item['suites'] = response['suites'][0],

        item['totalAreas'] = response['totalAreas'][0],
        item['usableAreas'] = response['usableAreas'][0],
        item['usageTypes'] = response['usageTypes'][0],
        yield item