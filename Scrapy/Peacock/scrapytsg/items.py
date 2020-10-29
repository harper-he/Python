# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import Compose, MapCompose, TakeFirst
from urllib.parse import urlparse
import os.path
import csv

# Extracts ID from URL 
def id_extractor(url):
    path = urlparse(url).path
    return os.path.split(path)[-1]

class PeacocktvTitle(scrapy.Item):
    id = scrapy.Field(
        input_processor=MapCompose(id_extractor),
        output_processor=TakeFirst()
    )
    platform = scrapy.Field(
        output_processor=TakeFirst()
    )
    name = scrapy.Field(
        output_processor=TakeFirst()
    )
    type = scrapy.Field(
        input_processor=MapCompose(type_cleaner),
        output_processor=TakeFirst()
    )
    genre = scrapy.Field(
        # input_processor=MapCompose(clean_genre),
        output_processor=Compose(remove_duplicates)
    )
    network = scrapy.Field(
        output_processor=TakeFirst()
    )
    tags = scrapy.Field()
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    contentrating = scrapy.Field(
        input_processor=MapCompose(clean_content_rating),
        output_processor=TakeFirst()
    )
    description = scrapy.Field(
        output_processor=TakeFirst()
    )
    airdate = scrapy.Field(
        output_processor=TakeFirst()
    )
    runtime = scrapy.Field(
        output_processor=TakeFirst()
    )
    numberofseasons = scrapy.Field(
        output_processor=TakeFirst()
    )
    actors = scrapy.Field()
    director = scrapy.Field()
    imageurl = scrapy.Field()
    image = scrapy.Field()
    country = scrapy.Field(
        input_processor=MapCompose(clean_country),
        output_processor=TakeFirst()
        )
    rawmetatags = scrapy.Field()
    trailerurl = scrapy.Field()
