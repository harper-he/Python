# peacocktv.py
import scrapy
from scrapy.loader import ItemLoader
from scrapytsg.items import PeacocktvTitle, id_extractor
import json
from urllib.parse import urlparse
import os.path
import csv

class PeacocktvSpider(scrapy.Spider):
    name = 'peacocktv'

    def import_list():
        with open('urls/peacocktv.csv', 'r', encoding='utf8') as f:
            str_list = [row[0] for row in csv.reader(f)]
        return(str_list)

    start_urls = import_list()

    def parse(self, response):
        # Script data from Peacocktv for scraping
        data = json.loads(response.css('script::text').getall()[1])
        javadata = response.css('script::text').getall()[2]
        loader = ItemLoader(item=PeacocktvTitle(), response=response)
        
        # Iterates over actors dict and returns list of names
        def actors_list(actors):
            actors_final = []
            for value in actors:
                actors_final.append(value['name'])
            return actors_final

        # Iterates over director dict and returns list of names
        def director_list(director):
            director_final = []
            for value in director:
                director_final.append(value['name'])
            return director_final

        # convert runtime 'PTxHyM' to milliseconds
        def runtime_to_milliseconds(t):
            h = int(t.split('PT')[1].split('H')[0])
            m = int(t.split('H')[1].split('M')[0])
            return int(3600000*h + 60000*m)

        # These fields are the same for both movie and tv
        # id, '@type', contentRating', 'description', 'genre', 'image', 'name', 'url', network
        try:
            loader.add_value('id', id_extractor(data['url']))
        except KeyError:
            pass 

        try:
            loader.add_value('platform', 'Peacock')
        except KeyError:
            pass    

        try:
            loader.add_value('type', data['@type'])
        except KeyError:
            pass    

        try:
            loader.add_value('name', data['name'])
        except KeyError:
            pass 

        try:
            loader.add_value('contentrating', data['contentRating'])
        except KeyError:
            pass

        try:
            loader.add_value('description', data['description'])
        except KeyError:
            pass

        try:
            loader.add_value('genre', data['genre'])
        except KeyError:
            pass

        try:
            loader.add_value('rawmetatags', data['genre'])
        except KeyError:
            pass

        try:
            network=javadata.split('"channelName":')[1].split(",")[0].strip('\"')
            loader.add_value('network', network)
        except KeyError:
            pass           

        try:
            loader.add_value('url', data['url']) # Yellowstone will return https://www.peacocktv.com/yellowstone
        except KeyError:
            pass 

        # try:
        #     loader.add_value('imageurl', data['image'])
        # except KeyError:
        #     pass

        if data['@type'] == 'Movie':

            try:
                loader.add_value('actors', actors_list(data['actor']))
            except KeyError:
                pass

            try:
                loader.add_value('airdate', data['copyrightYear'])
            except KeyError:
                pass

            try:
                loader.add_value('director', director_list(data['director']))
            except KeyError:
                pass

            try:
                loader.add_value('runtime', runtime_to_milliseconds(data['duration']))
            except KeyError:
                pass               

        else: # AKA if type is tv
            try:
                loader.add_value('actors', actors_list(data['actors']))
            except KeyError:
                pass    
            
            try:
                loader.add_value('numberofseasons', int(response.css('.asset-score > span::text').getall()[1].split()[0]))
            except KeyError:
                pass    

        yield loader.load_item()

        # number of seasons for 301 links path is: response.css('span.sk-color-white:nth-child(4)::text').get()
       
        # Json fields of movie & tv are:
        # # movie:
        # ['@context', '@id', '@type', 'actor', 'contentRating', 'copyrightYear', 'description', 'director', 'duration', 'genre', 'image', 'name', 'publisher', 'releasedEvent', 'reviewRating', 'thumbnailURL', 'url']
        # # tv
        # ['@context', '@type', 'actors', 'contentRating', 'description', 'genre', 'image', 'name', 'url']
