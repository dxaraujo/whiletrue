import scrapy
import json

from whiletrue.items import ZapItem

class ZapSpider(scrapy.Spider):

    name = 'zap'
    allowed_domains = ['glue-api.zapimoveis.com.br']
    # link = 'https://glue-api.zapimoveis.com.br/v2/listings?0=U&1=n&2=i&3=t&4=T&5=y&6=p&7=e&8=_&9=N&10=O&11=N&12=E&categoryPage=RESULT&business=SALE&listingType=USED&parentId=null&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=0&developmentsSize=0&superPremiumSize=0&addressCountry=&addressState=&addressCity=&addressZone=&addressNeighborhood=&addressStreet=&addressAccounts=&addressType=&addressLocationId=&addressPointLat=&addressPointLon=&__zt=lva:c,rnk_gz:rescore_ctr_default&size={0}&from={1}&page={2}'
    link = 'https://glue-api.zapimoveis.com.br/v2/listings?business=SALE&categoryPage=RESULT&parentId=null&listingType=USED&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=0&developmentsSize=0&superPremiumSize=0&addressCountry=&addressState=S%C3%A3o+Paulo&addressCity=S%C3%A3o+Paulo&addressZone=Zona+Leste&addressNeighborhood=Vila+Prudente&addressStreet=&addressAccounts=&addressType=neighborhood&addressLocationId=BR%3ESao+Paulo%3ENULL%3ESao+Paulo%3EZona+Leste%3EVila+Prudente&addressPointLat=-23.579014&addressPointLon=-46.579756&__zt=lva:c,rnk_gz:rescore_ctr_default&size={0}&from={1}&page={2}'
    start_urls = []

    size = 100
    for i in range(0, 100):
        start_urls.append(link.format(size, i * size, i + 1))

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        listings = jsonresponse['search']['result']['listings']
        for listing in listings:
            item = ZapItem()

            item['createdAt'] = listing['listing'].get('createdAt', '')
            item['title'] = listing['listing'].get('title', '')
            item['description'] = listing['listing'].get('description', '')

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

            point = listing['listing']['address'].get('point', '')
            print(point)
            if point:
                item['latitude'] = point['lat']
                item['longitude'] = point['lon']

            item['level'] = listing['listing']['address'].get('level', '')
            item['street'] = listing['listing']['address'].get('street', '')
            item['streetNumber'] = listing['listing']['address'].get('streetNumber', '')

            bathrooms = listing['listing'].get('bathrooms', '')
            if bathrooms:
                if len(bathrooms) > 0:
                    item['bathrooms'] = bathrooms[0],

            bedrooms = listing['listing'].get('bedrooms', '')
            if bedrooms:
                if len(bedrooms) > 0:
                    item['bedrooms'] = bedrooms[0],

            item['listingType'] = listing['listing'].get('listingType', '')

            parkingSpaces = listing['listing'].get('parkingSpaces', '')
            if parkingSpaces:
                if len(parkingSpaces) > 0:
                    item['parkingSpaces'] = parkingSpaces[0]

            suites = listing['listing'].get('suites', '')
            if suites:
                if len(suites) > 0:
                    item['suites'] = suites[0]

            totalAreas = listing['listing'].get('totalAreas', '')
            if totalAreas:
                if len(totalAreas) > 0:
                    item['totalAreas'] = totalAreas[0]

            usableAreas = listing['listing'].get('usableAreas', '')
            if usableAreas:
                if len(usableAreas) > 0:
                    item['usableAreas'] = usableAreas[0]

            usageTypes = listing['listing'].get('usageTypes', '')
            if usageTypes:
                if len(usageTypes) > 0:
                    item['usageTypes'] = usageTypes[0]

            yield item
        pass
