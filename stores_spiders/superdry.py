import scrapy
from selenium import webdriver
from scrapy import Request
import time
from scrapy.http import FormRequest ,TextResponse
class Super(scrapy.Spider):
	name = "superdry"
	start_urls = ['https://www.superdry.com/stores']
	def __init__(self, keyword=None, **kwargs):
		self.keyword = keyword
		self.driver = webdriver.Chrome()
	def parse(self,response):
		self.driver.get(response.url)
		new_dict = {}
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		city = self.driver.find_element_by_xpath('//input[@id="store_locator_address"]').click()
		time.sleep(2)
		# shop = self.driver.find_element_by_xpath('//span/a[@data-ga-label="buscarTiendas"]').click()
		# time.sleep(5)
		# cross2 = self.driver.find_element_by_xpath('//div[@class="search-input-clear"]').click()
		data = ['delhi','mumbai','gurgoan','noida','bhuvneshwar','hydrabad','chennai']
		for i in data:
			city = self.driver.find_element_by_xpath('//input[@id="store_locator_address"]').clear()
			city = self.driver.find_element_by_xpath('//input[@id="store_locator_address"]')
			city.send_keys(i)
			search = self.driver.find_element_by_xpath('//input[@value="Search"]').click()
			time.sleep(2)
			self.driver.get(response.url)
		 	selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
			address = selector.xpath('//div[@class="address"]/text()').extract()
			for j in address:
				new_dict["City"] = i
				new_dict["address"] = j
				yield new_dict
		