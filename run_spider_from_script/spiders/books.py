import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    custom_settings = {
        'FEEDS': {
            'books.csv': {
                'format': 'csv'
            }
        }

    }

    def parse(self, response):
        for s in response.xpath('//article')[:2]:
            yield {
                'title': s.xpath('.//h3/a/@title').get(),
                'price': s.xpath('.//p[@class="price_color"]/text()').get()
            }
        next_page = response.css('li.next > a::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
