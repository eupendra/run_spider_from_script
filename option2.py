from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from scrapy.utils.project import get_project_settings

from run_spider_from_script.spiders.books import BooksSpider
from run_spider_from_script.spiders.quotes import AllQuotesSpider
from scrapy.crawler import CrawlerRunner


def main():
    # Step 1
    configure_logging()

    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(BooksSpider)
    runner.crawl(AllQuotesSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()  # the script will block here until all crawling jobs are finished


if __name__ == '__main__':
    main()
