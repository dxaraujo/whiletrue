# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import psycopg2
import time

class WhiletruePipeline:
    def process_item(self, item, spider):
        return item

class PostgresPipeline:

    def open_spider(self, spider):
        hostname = '139.64.244.144'
        username = 'whiletrue'
        password = 'whiletrue'
        database = 'whiletrue'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if item['latitude'] != 0:
            queryTemplate = 'INSERT INTO ANUNCIOS(id_anuncios, createdAt, title, description, businessType, listingType, country, state, stateAcronym, city, zipCode, level, street, streetNumber, complement, latitude, longitude, bathrooms, bedrooms, suites, parkingSpaces, monthlyCondoFee, yearlyIptu, price, totalAreas, usableAreas, usageTypes, image, url, location) VALUES (nextval(\'anuncio_sq\'), \'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\', \'{7}\', \'{8}\', \'{9}\', \'{10}\', \'{11}\', \'{12}\', \'{13}\', \'{14}\', \'{15}\', \'{16}\', \'{17}\', \'{18}\', \'{19}\', \'{20}\', \'{21}\', \'{22}\', \'{23}\', \'{24}\', \'{25}\', \'{26}\', \'{27}\', {28})'
            query = queryTemplate.format(item['createdAt'], item['title'], item['description'], item['businessType'], item['listingType'], item['country'], item['state'], item['stateAcronym'], item['city'], item['zipCode'], item['level'], item['street'], item['streetNumber'], item['complement'], item['latitude'], item['longitude'], item['bathrooms'], item['bedrooms'], item['suites'], item['parkingSpaces'], item['monthlyCondoFee'], item['yearlyIptu'], item['price'], item['totalAreas'], item['usableAreas'], item['usageTypes'], item['image'], item['url'], 'ST_MakePoint({0}, {1})'.format(item['latitude'], item['longitude']))
            self.cur.execute(query)
            self.connection.commit()
        else:
            queryTemplate = 'INSERT INTO ANUNCIOS(id_anuncios, createdAt, title, description, businessType, listingType, country, state, stateAcronym, city, zipCode, level, street, streetNumber, complement, latitude, longitude, bathrooms, bedrooms, suites, parkingSpaces, monthlyCondoFee, yearlyIptu, price, totalAreas, usableAreas, usageTypes, image, url) VALUES (nextval(\'anuncio_sq\'), \'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\', \'{7}\', \'{8}\', \'{9}\', \'{10}\', \'{11}\', \'{12}\', \'{13}\', \'{14}\', \'{15}\', \'{16}\', \'{17}\', \'{18}\', \'{19}\', \'{20}\', \'{21}\', \'{22}\', \'{23}\', \'{24}\', \'{25}\', \'{26}\', \'{27}\')'
            query = queryTemplate.format(item['createdAt'], item['title'], item['description'], item['businessType'], item['listingType'], item['country'], item['state'], item['stateAcronym'], item['city'], item['zipCode'], item['level'], item['street'], item['streetNumber'], item['complement'], item['latitude'], item['longitude'], item['bathrooms'], item['bedrooms'], item['suites'], item['parkingSpaces'], item['monthlyCondoFee'], item['yearlyIptu'], item['price'], item['totalAreas'], item['usableAreas'], item['usageTypes'], item['image'], item['url'])
            self.cur.execute(query)
            self.connection.commit()
        time.sleep(0.1)
        return item