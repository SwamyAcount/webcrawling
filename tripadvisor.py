# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from scrapy.http import TextResponse


class TripadvisorSpider(scrapy.Spider):
	name = 'tripadvisor'
	allowed_domains = ['tripadvisor.com']
	start_urls = ['https://www.tripadvisor.co.uk/Restaurants-g297602-National_Capital_Territory_of_Delhi.html']

	# def __init__ (self, **kwargs):
	# 	self.driver = webdriver.Chrome()


	def parse(self, response):
		# self.driver.get(response.url)
		# time.sleep(7)
		# sel = TextResponse(url = response.url, body = self.driver.page_source, encoding = 'utf-8')

		pages_element = response.xpath('//div[@class="unified pagination js_pageLinks"]/div[@class="pageNumbers"]/a[@class="pageNum taLnk"]/text()').extract()
		print '---pages---',pages_element

		pages = pages_element[-1]
		pages = pages.replace('\n','')
		print '----',pages
		pages= int(pages)
		list = []
		s = 'https://www.tripadvisor.co.uk/Restaurants-g297602-National_Capital_Territory_of_Delhi.html#EATERY_LIST_CONTENTS'
		list.append(s)
		# print '--li----',list
		for i in range(1,pages):
			i = i * 30
			url = "https://www.tripadvisor.co.uk/Restaurants-g297602-oa" + str(i) + "-National_Capital_Territory_of_Delhi.html#EATERY_LIST_CONTENTS" 
			# print '------',url
			
			list.append(url)

		print '+++++',list
		for url in list:
			
			yield scrapy.Request(url = url,callback = self.product, dont_filter=True)
	def product(self, response):
	# 	# print '))))))))))))))))))))))))))'
	# 	# print '+++++',response.url
		product_url = response.xpath('//span/a[@class="restaurants-list-ListCell__restaurantName--2aSdo"]/@href').extract()
		# print '-product---',product_url
		result = 'https://www.tripadvisor.co.uk'
		for url in product_url:
			results = result + url
			print '----jjjjj-----',results
			yield scrapy.Request(url = results,callback = self.field, dont_filter=True,meta = {'asd':results})
	def field(self, response):
		# self.driver.get(response.url)
		# time.sleep(6)

		# self.driver.find_element_by_xpath('//div[@class="is-hidden-mobile blEntry website  ui_link"]/span[@class="detail "]').click()
		# time.sleep(8)
		product_name = response.xpath('//h1[@class="ui_header h1"]/text()').extract_first()
		print '-----',product_name

		address = response.xpath('//div[@class="is-hidden-mobile blEntry address  ui_link"]//span[@class="detail "]//span/text()').extract()
				  
		# print '-----add-----',address

		ad = ''.join(address) if address else None
		print '+++++++++',ad

		contact = response.xpath('//span[@class="detail  is-hidden-mobile"]/text()').extract_first()
		print '---con-----',contact

		new_dict = {'product_name':product_name,'address':address,'contact':contact}
		new_dict['results'] = response.meta['asd']

		# print '------',new_dict
		yield new_dict

		




