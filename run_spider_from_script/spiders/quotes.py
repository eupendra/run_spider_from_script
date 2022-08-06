import scrapy


class AllQuotesSpider(scrapy.Spider):
    name = 'all_quotes'
    start_urls = ['http://quotes.toscrape.com/']

    custom_settings = {
        'FEEDS': {
            'quotes.csv': {
                'format': 'csv'
            }
        }

    }
    def parse(self, response):
        for quote in response.css('.quote'):
            item = {
                'author': quote.css('.author ::text').get(),
                'title': quote.css('.text ::text').get(),
                'tags': quote.css('.tag ::text').get(),
            }

            yield item
        next_page = response.css('li.next > a::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
