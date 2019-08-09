# -*- coding: utf-8 -*-
import scrapy
# from selenium import webdriver
# import time
from scrapy import Request
from scrapy.http import TextResponse



class JustdailSpider(scrapy.Spider):
	name = 'justdail'
	# allowed_domains = ['justdail.com']
	start_urls = ['https://www.justdial.com/Delhi/Body-Massage-Centres-in-Delhi-High-Court/nct-10050521']

	# def __init__ (self, **kwargs):
	# 	self.driver = webdriver.Chrome()

	def parse(self, response):
		pages_element = response.xpath('//div[@class="jpag"]//a/text()').extract()
		# print '--pages------',pages_element
		
		pages = pages_element[-2]
		print '----',pages
		for i in range(1,60+1):
			url = 'https://www.justdial.com/Delhi/Body-Massage-Centres-in-Delhi-High-Court/nct-10050521/page-' + str(i)
			# print '------',url
			yield Request(url=url, callback=self.product)

	def product(self, response):
		# print '+++++++++++',response.url
		# self.driver.get(response.url)
		# time.sleep(5)
		product_url = response.xpath('//h2[@class="store-name"]/span[@class="jcn"]/a/@href').extract()
		# print '-----product------',product_url
		product = list(set(product_url))
		# print '++++++++',product
		for url in product:
			yield Request(url = url,callback = self.field)
			
	def field(self, response):
		# print '!!!!!!!!!!!',response.url
		company_name = response.xpath('//span[@class="fn"]/text()').extract()
		# print '---company------',company_name

		add = response.xpath('//span[@class="lng_add"]/text()').extract()
		# print '---------',add
		address = add[-1]
		# print '++++++++++',address

		new_dict = {'company_name':company_name,'address':address,'url':response.url}

		# print '------',new_dict
		yield new_dict



		

