import scrapy
from scrapy.http import Response

class ItemSpider(scrapy.Spider):
    name="itemspider"

    start_urls=[
        "https://books.toscrape.com/"
    ]

    def parse(self, response: Response):
        all_books_urls= response.css("ol.row li article.product_pod h3 a::attr(href)").getall()

        for url in all_books_urls:
           next_url=response.urljoin(url)
           yield scrapy.Request(url=next_url,callback=self.book_url)

    def book_url(self, response: Response):
        title=response.css("h1::text").get()
        prod_desc=response.css("p")[3].get()[3:-4]

        t_key=response.css("tr th::text").getall()
        t_val=response.css("tr td::text").getall()
        
        data={
            "title":title,
            "prod_desc":prod_desc,
        }
        table_dict=dict(zip(t_key,t_val))
        
        data.update(table_dict)
        yield data
