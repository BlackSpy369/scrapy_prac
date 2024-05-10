import scrapy
from scrapy.responsetypes import Response
import time
import random

class ProductsSpider(scrapy.Spider):
    name = "products"
    BASE_URL="https://www.amazon.in"

    
    def start_requests(self):
        products=["laptop"]

        for product in products:
            yield scrapy.Request(url=f"https://www.amazon.in/s?k={product}",callback=self.parse_pages)

    def parse_pages(self, response:Response):
        total_pages=int(response.css(".s-pagination-item.s-pagination-disabled::text").getall()[-1])
        for i in range(total_pages):
            yield scrapy.Request(url=response.url+f"&page={i+1}",callback=self.parse_links)
            # time.sleep(random.random())

    def parse_links(self,response:Response):
        links=response.css(".a-link-normal.a-text-normal::attr(href)").getall()

        for link in links:
            yield scrapy.Request(url=response.urljoin(link),callback=self.parse_product)       
            # time.sleep(random.random())
            
    def parse_product(self,response:Response):
            try:
                title=response.css("#productTitle::text").get().strip()
                price=response.css(".a-price-whole::text").get().strip()
                savings_per=response.css(".savingsPercentage::text").get().strip()

                yield {
                    "title":title,
                    "price":price,
                    "savings_per":savings_per,
                    "product_link":response.url,
                }
            except AttributeError:
                 self.logger.error("None type wala error h ye!")
