from scrapy.utils.project import get_project_settings

from run_spider_from_script.spiders.books import BooksSpider
from run_spider_from_script.spiders.quotes import AllQuotesSpider
from scrapy.crawler import CrawlerProcess


def main():
    # Step 1
    # process = CrawlerProcess()

    # Step 2
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(BooksSpider)
    process.crawl(AllQuotesSpider)
    process.start()  # the script will block here until the crawling is finished


if __name__ == '__main__':
    main()
