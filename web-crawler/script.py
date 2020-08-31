# https://dev.to/pjcalvo/broken-links-checker-with-python-and-scrapy-webcrawler-1gom

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field

# Scrapy.CrawlSpider require that we return an Item object, 
# this will contain the data that will be reported.
class MyItems(Item):
    referer = Field()
    response = Field()
    status = Field()
# The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. 
# Spiders may return the extracted data as items, Python objects that define key-value pairs.
# fields: 
# A dictionary containing all declared fields for this Item, not only those populated. The keys are the field names and the values are the Field objects used in the Item declaration.
## eg:
# class CustomItem(Item):
#     one_field = Field()
#     another_field = Field()
# Field objects are used to specify metadata for each field.


class MySpider(CrawlSpider):
    # CrawlSpider is the most commonly used spider for crawling regular websites
    # it provides a convenient mechanism for following links by defining a set of rules.
    name = 'test-crawler' # A string which defines the name for this spider. 
                          # it must be unique
                          # If the spider scrapes a single domain, a common practice is to name the spider after the domain
    target_domains = ["beta.thestreamingguide.com"]  # =allowed_domains
                         # list of domains that will be allowed to be crawled
    start_urls = ["https://beta.thestreamingguide.com/"]
                          # A list of URLs where the spider will begin to crawl from, when no particular URLs are specified.
    handle_httpstatus_list = [404, 410, 301, 500] # only 200 by default. you can add more status to list
                             # 301 Moved Permanently
                             # 410 Gone: access to the target resource is no longer available at the origin server and that this condition is likely to be permanent.
                             # 500 Internal Server Error: The server has encountered a situation it doesn't know how to handle.
    custom_settings = {
        'CONCURRENT_REQUESTS': 2, # The maximum number of concurrent (i.e. simultaneous) requests that will be performed by the Scrapy downloader.
        'DOWNLOAD_DELAY': 0.5     # The amount of time (in secs) that the downloader should wait before downloading consecutive pages from the same website. This can be used to throttle the crawling speed to avoid hitting servers too hard. Decimal numbers are supported. 
    }
                          # A dictionary of settings that will be overridden from the project wide configuration when running this spider.

    rules = [
        Rule(
            # Extract links matching target_domains  (but not matching 'patterToBeExcluded')
            LinkExtractor(allow_domains=target_domains,deny=('patterToBeExcluded'), unique=('Yes')),
            # parse them with the method parse_my_url
            callback = 'parse_my_url',
            follow = True
            # extract all unique links under the target_domains and follow them, 
            # but exclude those who contains patterToBeExcluded.
        ),
        Rule(
            # crawl external links but don't follow them
            LinkExtractor(allow=(''),deny=('patterToBeExcluded'), unique=('Yes')),
            callback = 'parse_my_url',
            follow = False
            # extract all unique links but do not follow them and exclude those who contains patterToBeExcluded.
        )
    ]
    # A list of one (or more) Rule objects. 
    # Each Rule defines a certain behaviour for crawling the site. 
    # If multiple rules match the same link, the first one will be used, according to the order they’re defined in this attribute.



# The callback:  process downloaded responses
# The parse method is in charge of processing the response and returning scraped data and/or more URLs to follow.
# This method must return an iterable of Request and/or item objects. 
# This is the method that will be called for each link that gets requested. 
# every item that will be returned will be added to the csv report. 
# so here is where can filter out only what we need to report.
    def parse_my_url(self, response):
        # list of response codes that we want to include on the report, we know that 404
        report_if = [404]
        if response.status in report_if: # if the response matches then creates a MyItem
            item = MyItems()
            item['referer'] = respnse.request.headers.get('Referer', None)
            item['status'] = response.status
            item['response'] = response.url
            yield item
        yield None # if the response did not match return empty
# everytime the web crawler hits a page and response 404 then a row will be added to the csv report. 
# modify this list as requested.

# Running the crawler
# $ scrapy runspider script.py -o report-file.csv
