import scrapy
from weather.items import WeatherItem
import json



class WeathersSpider(scrapy.Spider):
    name = 'weathers'
    allowed_domains = ['weather.com']
    start_urls = ['http://weather.com/']



    def start_requests(self):
        urls=[
            "https://weather.com/en-IN/weather/today/l/f42d9f8baa19b4d8d5e034449faa703839993366f64551a56a2b530297075dc2",
            "https://weather.com/en-IN/weather/today/l/f8a5e3f7403d62a7f8a3c34e16f6bdec6762e2c6a7255e58c39750895764f9b2",
            "https://weather.com/en-IN/weather/today/l/fc317921b24846366d16f1a064dcfc1b99e07ed74dbf2e7e774384f551ede2de",
            "https://weather.com/en-IN/weather/today/l/1f69f55773d58b72525ca4cc565ee72e7fdb3adc0c4506a0db6e03a16cd82d52",
            "https://weather.com/en-IN/weather/today/l/777f2128f8d768a75917b81b6f19230d565914268623669b00afe75564c5d7d4",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):


        city=response.xpath('//h1[contains(@class,"location")]/text()').get()
        temperature=response.xpath('//span[contains(@class,"tempValue")]/text()').get()
        conditions=response.xpath('//div[contains(@class,"phraseValue")]/text()').get()
        visibility=response.xpath('//div[contains(@class, "WeatherDetailsListItem--wxData--kK35q")]//span[contains(@data-testid, "VisibilityValue")]/text()').get()
        wind=response.xpath('//div[contains(@class, "WeatherDetailsListItem--wxData--kK35q")]//span[contains(@class, "Wind--windWrapper--3Ly7c undefined")]/text()').get()
                        
        print(city, temperature,visibility,wind,conditions)

        yield WeatherItem(
            city=city,
            temperature=temperature,
            conditions=conditions,
            visibility=visibility,
            wind=wind
            
        )

     
