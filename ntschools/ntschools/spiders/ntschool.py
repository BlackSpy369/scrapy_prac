import scrapy

class NtschoolSpider(scrapy.Spider):
    name = "ntschool"
    start_urls = ["https://directory.ntschools.net/#/schools/"]
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,lb;q=0.7",
        "Referer": "https://directory.ntschools.net/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "X-Requested-With": "Fetch",
    }
    def parse(self, response):
        url="https://directory.ntschools.net/api/System/GetAllSchools"

        yield scrapy.Request(url=url,headers=self.headers,callback=self.parse_data)
    
    def parse_data(self,response):
        base_url="https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="
        data=response.json()

        for school in data:
            it_school_code=school["itSchoolCode"]
            school_data_url=base_url+it_school_code
            yield scrapy.Request(url=school_data_url,headers=self.headers,callback=self.parse_school)

    def parse_school(self,response):
        data=response.json()

        yield {
            "name":data["name"],
            "region": data["region"],
            "physicalAddress":data["physicalAddress"],
            "postalAddress":data["postalAddress"],
            "ntgGeographicDefinition": data["ntgGeographicDefinition"],
            "preSchool": data["preSchool"],
            "primarySchool": data["primarySchool"],
            "middleSchool": data["middleSchool"],
            "seniorSchool": data["seniorSchool"],
            "telephoneNumber": data["telephoneNumber"], 
        }

