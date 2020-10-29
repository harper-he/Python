### Task:</br>
Scrape the content on Peacock.</br>
Index all Peacock URLs and scrape them for relevant content to populate our platform. 

### Steps:</br>
Index URLs:</br>
1. Go to https://www.peacocktv.com/sitemap.xml and download the sitemap-1.xml(movie) and sitemap-2.xml(tv)
2. urlgen/generators/peacocktv.py takes the XML documents and returns Python objects which mirrors the nodes and attributes in theis structure for future use.
3. The output text file of URLs are at 'urlgen/outputs/'
4. Clean the URLs in EXCEL and save it as CSV file in '/scrapytsg/urls/'
Crawl:
5. Go to '/scrapytsg/spiders/peacocktv.py' and run command 'scrapy crawl peacocktv -o testcode.json'. This will generate an json file containing all scraped items, serialized in JSON.
6. Check output in 'scrapytsg/outputs/peacock09.29.2020.json'.

Though most fields are scraped from the json file of the website, the field "network" and "number of seasons" are scraped from javascript.

Some urls are redirected to other pages. 17 urls have status_code as 301, meaning they are redirected to another link. Though these pages are accessible, the infromation is located somewhere else so we cannot extract with current codes. To solve this problem, we can either create logical conditions like if requests.get(url).status_code == 301 ... else ...
or we can manually update the filed data from javascript.

More than 60 urls with code '302' are redirected to '/unavailable' url. 

I successfully scraped 1000 out of 1120 movies, and identified the items that could not be scraped so that we could fix them manually afterwards. It greatly expanded the number of content on our platform and would be a great update in our next release.
