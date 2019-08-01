import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Request
import time
from scrapy.http import FormRequest ,TextResponse
class Super(scrapy.Spider):
	name = "levis"
	start_urls = ['https://www.levi.in/stores']
	def __init__(self, keyword=None, **kwargs):
		self.keyword = keyword
		self.driver = webdriver.Chrome()
	def parse(self,response):
		self.driver.get(response.url)
		new_dict = {}
		a = []
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		city = selector.xpath('//select[@name="storeStates"]/option/text()').extract()
		for j in city:
			j = j.replace('\n','')
			j = str(j)
			j.strip()
			a.append(j)
			if 'Select City' in a:
				a.remove('Select City')
		
		for i in a:
			i = "'"+i+"'"
			self.driver.get(response.url)
			time.sleep(3)
			body = self.driver.find_element_by_tag_name('body')
			body.send_keys(Keys.HOME)
			time.sleep(1)

			input_city = self.driver.find_element_by_xpath('//span[@class="ui-selectmenu-text"]').click()
			time.sleep(2)
			city = self.driver.find_element_by_xpath("//li[@class='ui-menu-item']/div[contains(text(),"+i+")]").click()
			time.sleep(1)
			search = self.driver.find_element_by_xpath('//button[@class="searchByCity"]').click()
			time.sleep(2)
			selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
			address = selector.xpath('//div[@class="store-address"]//div[1]/text()').extract()
			
			for add in address:
				new_dict["City"] = i
				new_dict["Address"] = add
				yield new_dict








