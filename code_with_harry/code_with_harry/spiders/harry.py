import scrapy
from scrapy.responsetypes import Response

class HarrySpider(scrapy.Spider):
    name = "harry"
    start_urls = ["https://www.codewithharry.com"]
    api_url="https://www.codewithharry.com/_next/data/mTRMPr4jUfRMmKDoT9TYy/"
    api_url_2="https://www.codewithharry.com/_next/data/mTRMPr4jUfRMmKDoT9TYy/tutorial/"

    def parse(self, response:Response): 
        all_tuts=response.css("li a::attr(href)").getall()[8:-5]

        for tut in all_tuts:
            next_url=self.api_url+tut[:-1]+".json"
            yield scrapy.Request(url=next_url,callback=self.parse_tut)

    def parse_tut(self,response:Response):
        data=response.json()
        for key in data["pageProps"]["tutorials"].keys():
            for d in data["pageProps"]["tutorials"][key]:
                # all_slugs.append(d["slug"])
                next_url=self.api_url_2+d["slug"]+".json"
                yield scrapy.Request(url=next_url,callback=self.parse_tut_json)
        

    def parse_tut_json(self,response:Response):
        data=response.json()
        content_json=data["pageProps"]["tutorial"]

        yield{
            "title":content_json["title"],
            "content":content_json["content"]
        }

