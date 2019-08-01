import scrapy
from selenium import webdriver
from scrapy import Request
import time
from scrapy.http import FormRequest ,TextResponse

class Super(scrapy.Spider):
	name = "satyapaul"
	start_urls = ['http://store.satyapaul.com/']
	def __init__(self, keyword=None, **kwargs):
		self.keyword = keyword
		self.driver = webdriver.Chrome()

	def parse(self,response):
		self.driver.get(response.url)
		time.sleep(3)
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		href = selector.xpath('//li[@class="city-bar"]/a/@href').extract()
		city = selector.xpath('//li[@class="city-bar"]/a/text()').extract()
		
		for i in href:
			for c in city:
				if c.lower().strip().replace(' ','') in i.replace('-',''):
		
					url= i
					yield Request(url= url, callback= self.parse2 ,meta={"city":c})
	def parse2(self,response):
		new_dict = {}
		city = response.meta["city"]
		address = response.xpath('//span[@class="store-location"]/text()').extract()
		for add in address:

			new_dict['City'] = city
			new_dict['Address'] = add

			yield new_dict

