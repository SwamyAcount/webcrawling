import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Request
import time
from scrapy.http import FormRequest ,TextResponse
class Super(scrapy.Spider):
	name = "raymond"
	start_urls = ['https://www.snapdeal.com/products/men-sports-tshirts-polos?sort=plrty']
	def __init__(self, keyword=None, **kwargs):
		self.keyword = keyword
		self.driver = webdriver.Chrome()
	def parse(self,response):
		self.driver.get(response.url)
		new_dict = {}
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		# search = self.driver.find_element_by_xpath('//*[@id="panel"]/form/div[1]/input').click()
		href = selector.xpath('//a[@class="dp-widget-link hashAdded"]/@href').extract()
		print(href)
		for i in href:
			yield Request(url = i, callback = self.parse2)
	def parse2(self,response):
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		new_dict = {}
		name = selector.xpath('//h1[@itemprop="name"]//text()').extract()
		price = selector.xpath('//span[@class="payBlkBig"]//text()').extract()



		new_dict['Name'] = name
		new_dict['Price'] = price
		yield new_dict

































		# shop = self.driver.find_element_by_xpath('//span/a[@data-ga-label="buscarTiendas"]').click()
		# time.sleep(5)
		# cross2 = self.driver.find_element_by_xpath('//div[@class="search-input-clear"]').click()
		# time.sleep(1)
		# city = self.driver.find_element_by_xpath('//*[@id="panel"]/form/div[1]/input').click()
		# data = ["guntur", "vijayawada", "vizag", "vishakapatnam", "warangal", "guwahati", "patna", "chandigarh", "bhilai", 
		#  "durg", "raipur","delhi", "panjim", "ahmedabad", "baroda", "jamnagar", "rajkot", "surat", "vadodara","gurgaon", 
		#  "faridabad","kurukshetra", "simla", "jammu", "srinagar", "dhanbad", "jamshedpur", "ranchi","bengaluru", "belgaum", "hubli", "dhanbad", 
		#  "mangalore", "mysore", "calicut", "cochin", "kozhikode", "kannur", "kollam", "kottayam", "palakkad", "thrissur", 
		#  "thiruvanathpuram", "bhopal", "gwalior", "indore", "jabalpur","mumbai","pune", "amravati", "aurangabad", "bhiwandi", "chinchwad", 
		#  "kolhapur", "nagpur", "nashik", "solapur", "thane", "cuttack", "bhubaneswar", "amritsar", "bhathinda", "jalandhar", 
		#  "ludhina", "mohali", "patiala", "pondicherry", "bikaner", "jaipur", "jodhpur", "kota", "udaipur","chennai", "coimbatore", 
		#  "madurai", "salem", "tiruchirappalli", "tiruppur","hyderabad", "secundrabad","noida", "agra", "aligarh", "allahabad", "bareilly", 
		#  "ghaziabad", "gorakhpur", "kanpur", "lucknow", "meerut", "moradabad", "varanasi", "dehradun", "haldwani","kolkata", "asansol", 
		#  "durgapur", "siliguri"]
		# for i in data:
		# 	city = self.driver.find_element_by_xpath('//*[@id="panel"]/form/div[1]/input').clear()
		# 	city = self.driver.find_element_by_xpath('//*[@id="panel"]/form/div[1]/input')
		# 	city.send_keys(i)
		# 	city.send_keys(Keys.ENTER)
		# 	time.sleep(4)
		# 	selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		# 	address_info = selector.xpath('//div[@class="address"]/text()[1]').extract()
		# 	for j in address_info:
		# 		new_dict["City"] = i
		# 		new_dict["address"] = j
		# 		yield new_dict

