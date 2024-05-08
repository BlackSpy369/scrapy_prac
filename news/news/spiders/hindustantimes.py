import scrapy


class HindustantimesSpider(scrapy.Spider):
    name = "hindustantimes"
    start_urls = ["https://www.hindustantimes.com/"]

    def parse(self, response):
        BASE_URL="https://www.hindustantimes.com/"

        all_articles_link=response.css(".\hdg3 a::attr(href)").getall()
        for article_link in all_articles_link:
            yield scrapy.Request(url=BASE_URL+article_link,callback=self.parse_article)

    def parse_article(self,response):
        yield {
            "title":response.css(".hdg1::text").get(),
            "short_desc":response.css(".sortDec::text").get(),
            "body":"\n".join(response.css(".detail p::text").getall())
        }