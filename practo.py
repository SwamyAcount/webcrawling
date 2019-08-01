# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from scrapy.http import TextResponse

class PractoSpider(scrapy.Spider):
	name = 'practo'
	allowed_domains = ['practo.com']
	start_urls = ['https://www.practo.com/delhi/dietitian-nutritionist']

	def __init__ (self, **kwargs):
		self.driver = webdriver.Chrome()
		
	def parse(self,response):
		self.driver.get(response.url)
		time.sleep(8)
		sel = TextResponse(url = response.url, body = self.driver.page_source, encoding = 'utf-8')
		# total_products = sel.path('//h4[@class="u-d-inlineblock u-smallest-font implicit subsection"]/span[@data-qa-id="results_count"]/text()').extract_first()
		# print '---total--',total_products
		# sel = TextResponse(url = response.url, body = self.driver.page_source, encoding = 'utf-8')

		pages_element = sel.xpath('//div[@class="pure-u-14-24"]/ul[@class="c-paginator"]/li[@class=""]/a/text()').extract_first()
		# print '+++pages++++',pages_element
		pages_element= int(pages_element)
		for i in range(1,18+1):
			url = 'https://www.practo.com/delhi/dietitian-nutritionist?page=' + str(i)
			print '------',url
			yield scrapy.Request(url = url, callback = self.product)
	def product(self,response):
		self.driver.get(response.url)
		sel = TextResponse(url = response.url, body = self.driver.page_source, encoding = 'utf-8')
		product_url = sel.xpath('//a[@class="u-color--primary"]/@href').extract()
		# print '----product_url-----',product_url
		result = 'https://www.practo.com'
		for url in product_url:
			results = result + url
			print '---jjjj-',results
			yield scrapy.Request(url = results,callback = self.asd,dont_filter = True,meta = {'field':results})
	def asd(self,response):
		
		doctor_name = response.xpath('//h1[@data-qa-id="doctor-name"]/text()').extract_first()
		# print '++doctor+++',doctor_name
		if not doctor_name:
			doctor_name = response.xpath('//h1[@class="c-profile__title u-bold u-d-inlineblock"]/text()').extract_first()
			print '----doctor---',doctor_name
		description = response.xpath('//p[@class="c-profile__description"]/text()').extract_first()
		description = description.strip() if description else None
		# print '---des---',description

		address = response.xpath('//p[@class="c-profile--clinic__address"]/text()').extract_first()
		print '++++add++++',address

		new_dict = {'doctor_name':doctor_name,'description':description,'address':address}
		new_dict['results'] = response.meta['field']

		# print '------',new_dict
		yield new_dict



		


		
