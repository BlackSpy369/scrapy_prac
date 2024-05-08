import scrapy


class BowlingSpider(scrapy.Spider):
    name = "bowling"
    start_urls = ["https://indianexpress.com/section/sports/ipl/"]

    def parse(self, response):
        attr=response.css("#iplStats-2 .constituency-list__th .table-data::text").getall()
        attr.insert(0,"NAME")

        for i in response.css("#iplStats-2 .constituency-list__tr"):
            player_name=i.css(".i-team-name::text").get()
            data=[]
            for j in  i.css(".table-data::text").getall()[3:]:
                if j not in [" ","\n"]:
                    data.append(j)
            data.insert(0,player_name)
            yield dict(zip(attr,data))
