import scrapy
from scrapy.http import Response

class BioSpider(scrapy.Spider):
    name="biospider"

    start_urls=["https://en.wikibooks.org/wiki/Wikijunior:Biology"]
   
    def parse(self, response: Response):
        BASE_URL="https://en.wikibooks.org/"
        all_links=response.css("ol li ol li a::attr(href)").getall()

        for link in all_links:
            yield scrapy.Request(url=f"{BASE_URL}{link}",callback=self.web_page_scrapper)
    
    def web_page_scrapper(self,response:Response):
        for i in response.css("p").getall():
         if i!="\n":
            file_name=response.css("h1 span::text")[2].get().split("/")[-1]
            with open('data/'+file_name+'.txt',"a") as f:
               f.write(i)
