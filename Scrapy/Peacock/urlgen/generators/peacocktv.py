# peacocktv.py
import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
from pysitemap import crawler

if __name__ == '__main__':

    url_list = []

    tree = ET.parse('sitemap-1.xml')
    root = tree.getroot()

    for child in root:
        url_list.append(child[0].text)

    today=date.today()
    d=today.strftime("%m.%d.%y")
    with open(f'../outputs/peacocktv1-{d}.txt', "w") as outfile:
        for i in url_list:
            outfile.write('%s\n' % i)
# the url_list above creates all the urls of movies
    
    url_list2 = []
    tree2 = ET.parse('sitemap-2.xml')
    root2 = tree2.getroot()

    for child in root2:
        url_list2.append(child[0].text)

    with open(f'../outputs/peacocktv2-{d}.txt', "w") as outfile:
        for i in url_list2:
            outfile.write('%s\n' % i)
        
# the url_list above creates all the urls of tv

### The mothod below works with most urls but there are always 3 urls raising errors 
# import sys
# from datetime import date
# import logging
# from pysitemap import crawler

# if __name__ == '__main__':
#     if '--iocp' in sys.argv:
#         from asyncio import events, windows_events
#         sys.argv.remove('--iocp')
#         logging.info('using iocp')
#         el = windows_events.ProactorEventLoop()
#         events.set_event_loop(el)

#     # root_url = sys.argv[1]
#     root_url = 'https://www.peacocktv.com/'
#     today = date.today()
#     d = today.strftime("%m.%d.%y")
#     crawler(root_url, out_file=f'/Users/harperhe/Documents/Vale/Github/scrapy-tsg/urlgen/outputs/peacocktv{d}.txt', out_format='txt')
