import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from scrapy.http import TextResponse


class AllensollySpider(scrapy.Spider):
	name = "louisphilippe"
	# allowed_domains = ["AllenSolly.com"]
	start_urls = ['https://www.louisphilippe.com/content/store-locators-9']

	def __init__ (self,state = None, **kwargs):
		self.driver = webdriver.Chrome()
		self.state = state



	def parse(self, response):
		self.driver.get(response.url)
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		# element = selector('//select[@class="form-control state"]').click()
		
		time.sleep(5)
		store = []
		store_data = {}
		state = ["andhra pradesh","assam","bihar","chandigarh","chhattisgarh","delhi","goa","gujarat","haryana","himachal","jammu","jharkhand",
		   "karnataka","kerala","madhya pradesh","maharashtra","orissa","punjab","pondicherry","rajasthan","tamil nadu",
		   "telangana","uttar pradesh","uttarakhand","west bengal",]
		data = ["guntur", "vijayawada", "vizag", "vishakapatnam", "warangal", "guwahati", "patna", "chandigarh", "bhilai", 
		 "durg", "raipur","delhi", "panjim", "ahmedabad", "baroda", "jamnagar", "rajkot", "surat", "vadodara","gurgaon", 
		 "faridabad","kurukshetra", "simla", "jammu", "srinagar", "dhanbad", "jamshedpur", "ranchi","bengaluru", "belgaum", "hubli", "dhanbad", 
		 "mangalore", "mysore", "calicut", "cochin", "kozhikode", "kannur", "kollam", "kottayam", "palakkad", "thrissur", 
		 "thiruvanathpuram", "bhopal", "gwalior", "indore", "jabalpur","mumbai","pune", "amravati", "aurangabad", "bhiwandi", "chinchwad", 
		 "kolhapur", "nagpur", "nashik", "solapur", "thane", "cuttack", "bhubaneswar", "amritsar", "bhathinda", "jalandhar", 
		 "ludhina", "mohali", "patiala", "pondicherry", "bikaner", "jaipur", "jodhpur", "kota", "udaipur","chennai", "coimbatore", 
		 "madurai", "salem", "tiruchirappalli", "tiruppur","hyderabad", "secundrabad","noida", "agra", "aligarh", "allahabad", "bareilly", 
		 "ghaziabad", "gorakhpur", "kanpur", "lucknow", "meerut", "moradabad", "varanasi", "dehradun", "haldwani","kolkata", "asansol", 
		 "durgapur", "siliguri",]
		for element in state:
			if element:

				city = self.driver.find_elements_by_xpath('//select[@class="form-control state"]/option')
				for c in city:
					state =  c.text
					if element == state.lower():
						c.click()
						time.sleep(6)

						for a in data:
							if a:
								state = self.driver.find_elements_by_xpath('//select[@class="form-control city"]/option')
								for r in state:
									city = r.text
									if a == city.lower():
										r.click()
										search = self.driver.find_element_by_xpath('//button[@class="orange_btn btn"]').click()
										time.sleep(6)
										selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
										add = selector.xpath('//div[@class="store_locator_add"]/p/span/text()').extract()
										store.append(add)
		for ele in data:
			for s in store:
				if len(store) > 1:
					# for b in store:
					add = "".join(s).strip()
					if ele.lower() in add.lower():
						store_data['city'] = ele
						store_data['add'] = add.replace('\n','')
						print store_data
						yield store_data
				else:
					add = "".join(s).strip()
					if ele.lower() in add.lower():
						store_data['city'] = ele
						store_data['add'] = add.replace('\n','')
						print store_data
						yield store_data





# import scrapy
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from scrapy.http import TextResponse


# class AllensollySpider(scrapy.Spider):
# 	name = "AllenSolly"
# 	allowed_domains = ["AllenSolly.com"]
# 	start_urls = ['https://www.allensolly.com/content/store-locators-9']

# 	def __init__ (self,state = None, **kwargs):
# 		self.driver = webdriver.Chrome()
# 		self.state = state



# 	def parse(self, response):
# 		self.driver.get(response.url)
# 		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
# 		# element = selector('//select[@class="form-control state"]').click()
		
# 		time.sleep(8)
# 		store = []
# 		store_data = {}
# 		state = ["andhra pradesh","assam","bihar","chandigarh","chhattisgarh","delhi","goa","gujarat","haryana","himachal","jammu","jharkhand",
# 		   "karnataka","kerala","madhya pradesh","maharashtra","orissa","punjab","pondicherry","rajasthan","tamil nadu",
# 		   "telangana","uttar pradesh","uttarakhand","west bengal",]
# 		data = ["guntur", "vijayawada", "vizag", "vishakapatnam", "warangal", "guwahati", "patna", "chandigarh", "bhilai", 
# 		 "durg", "raipur","delhi", "panjim", "ahmedabad", "baroda", "jamnagar", "rajkot", "surat", "vadodara","gurgaon", 
# 		 "faridabad","kurukshetra", "simla", "jammu", "srinagar", "dhanbad", "jamshedpur", "ranchi","bengaluru", "belgaum", "hubli", "dhanbad", 
# 		 "mangalore", "mysore", "calicut", "cochin", "kozhikode", "kannur", "kollam", "kottayam", "palakkad", "thrissur", 
# 		 "thiruvanathpuram", "bhopal", "gwalior", "indore", "jabalpur","mumbai","pune", "amravati", "aurangabad", "bhiwandi", "chinchwad", 
# 		 "kolhapur", "nagpur", "nashik", "solapur", "thane", "cuttack", "bhubaneswar", "amritsar", "bhathinda", "jalandhar", 
# 		 "ludhina", "mohali", "patiala", "pondicherry", "bikaner", "jaipur", "jodhpur", "kota", "udaipur","chennai", "coimbatore", 
# 		 "madurai", "salem", "tiruchirappalli", "tiruppur","hyderabad", "secundrabad","noida", "agra", "aligarh", "allahabad", "bareilly", 
# 		 "ghaziabad", "gorakhpur", "kanpur", "lucknow", "meerut", "moradabad", "varanasi", "dehradun", "haldwani","kolkata", "asansol", 
# 		 "durgapur", "siliguri",]
# 		for element in state:
# 			if element:

# 				city = self.driver.find_elements_by_xpath('//select[@class="form-control state"]/option')
# 				for c in city:
# 					state =  c.text
# 					if element == state.lower():
# 						c.click()
# 						time.sleep(6)
						
# 						for a in data:
# 							if a:
# 								state = self.driver.find_elements_by_xpath('//select[@class="form-control city"]/option')
# 								for r in state:
# 									city = r.text
# 									if a == city.lower():
# 										r.click()
# 										search = self.driver.find_element_by_xpath('//button[@class="orange_btn btn"]').click()
# 										time.sleep(6)
# 										selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
# 										add = selector.xpath('//div[@class="store_locator_add"]/p/span/text()').extract()
# 										store.append(add)
# 		for ele in data:
# 			for s in store:
# 				if len(store) > 1:
# 					# for b in store:
# 				    add = "".join(s).strip()
# 					if ele.lower() in add.lower():
# 						store_data['city'] = ele
# 						store_data['add'] = add.replace('\n','')
# 						print store_data
# 						yield store_data
# 				else:
# 					add = "".join(s).strip()
# 					if ele.lower() in add.lower():
# 						store_data['city'] = ele
# 						store_data['add'] = add.replace('\n','')
# 						print store_data
# 						yield store_data