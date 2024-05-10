
BOT_NAME = "amazon_scraping"

SPIDER_MODULES = ["amazon_scraping.spiders"]
NEWSPIDER_MODULE = "amazon_scraping.spiders"


ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"




# SCRAPEOPS_API_KEY = '252adf78-be51-4733-b1c5-f56ddaa10124'
# SRAPEOPS_PROXY_ENABLED=True

# EXTENSIONS = {
#     'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
# }
# DOWNLOADER_MIDDLEWARES = {
#     'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
# }   

CONCURRENT_REQUESTS=2


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

