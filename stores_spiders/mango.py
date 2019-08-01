import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Request
import time
from scrapy.http import FormRequest ,TextResponse
class Super(scrapy.Spider):
	name = "mango"
	start_urls = ['https://shop.mango.com/in']
	def __init__(self, keyword=None, **kwargs):
		self.keyword = keyword
		self.driver = webdriver.Chrome()
	def parse(self,response):
		self.driver.get(response.url)
		new_dict = {}
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		cross = self.driver.find_element_by_xpath('//span[@class="modal-close-icon"]').click()
		time.sleep(6)
		shop = self.driver.find_element_by_xpath('//span/a[@data-ga-label="buscarTiendas"]').click()
		time.sleep(5)
		cross2 = self.driver.find_element_by_xpath('//div[@class="search-input-clear"]').click()
		time.sleep(1)
		city = self.driver.find_element_by_xpath('//input[@class="sg-p-inp search-input"]').click()
		data = ["guntur", "vijayawada", "vizag", "vishakapatnam", "warangal", "guwahati", "patna", "chandigarh", "bhilai", 
		 "durg", "raipur","delhi", "panjim", "ahmedabad", "baroda", "jamnagar", "rajkot", "surat", "vadodara","gurgaon", 
		 "faridabad","kurukshetra", "simla", "jammu", "srinagar", "dhanbad", "jamshedpur", "ranchi","bengaluru", "belgaum", "hubli", "dhanbad", 
		 "mangalore", "mysore", "calicut", "cochin", "kozhikode", "kannur", "kollam", "kottayam", "palakkad", "thrissur", 
		 "thiruvanathpuram", "bhopal", "gwalior", "indore", "jabalpur","mumbai","pune", "amravati", "aurangabad", "bhiwandi", "chinchwad", 
		 "kolhapur", "nagpur", "nashik", "solapur", "thane", "cuttack", "bhubaneswar", "amritsar", "bhathinda", "jalandhar", 
		 "ludhina", "mohali", "patiala", "pondicherry", "bikaner", "jaipur", "jodhpur", "kota", "udaipur","chennai", "coimbatore", 
		 "madurai", "salem", "tiruchirappalli", "tiruppur","hyderabad", "secundrabad","noida", "agra", "aligarh", "allahabad", "bareilly", 
		 "ghaziabad", "gorakhpur", "kanpur", "lucknow", "meerut", "moradabad", "varanasi", "dehradun", "haldwani","kolkata", "asansol", 
		 "durgapur", "siliguri"]
		for i in data:
			
			city = self.driver.find_element_by_xpath('//input[@class="sg-p-inp search-input"]')
			city.send_keys(i)
			city.send_keys(Keys.ENTER)
			time.sleep(3)
		 	selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')

			address_info = selector.xpath('//ul[@class="store-info"]')
			
			for element in address_info:
				address = element.xpath('.//text()').extract()
				address = address[:2]
				# print("================================",address)
				# address = str(address)
				address = ",".join(address).lower().strip()
				# address_details = selector.xpath('//li[@class="store-info-address"]//text()').extract()
				if (i in address):
					# print(address,i)

				# for j in address_details:
					# for j in address:
						# if (i in address):
					new_dict["City"] = i
					new_dict["Address"] = address
					yield new_dict				
			cross2 = self.driver.find_element_by_xpath('//div[@class="search-input-clear"]').click()
						