# -*- coding: utf-8 -*-
import scrapy


class GlasesSpider(scrapy.Spider):
    name = 'Glases'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath('//div[@id="product-lists"]/div')
        
        for product in products:
            yield {
                'Product ' : product.xpath('.//div[@class="p-title"]/a/@title').get(),
                'Link' : product.xpath('.//div[@class="p-title"]/a/@href').get(),
                'Product Image url' : product.xpath('.//div[@class="product-img-outer"]/a/img[1]/@src').get(),
                'Price' : product.xpath('.//div[@class="p-price"]/div/span/text()').get()

                }
        
        next_page = response.xpath('//ul[@class="pagination"]/li[position() = last()]/a/@href').get()
        
        if next_page:
           yield scrapy.Request(url=next_page, callback=self.parse)
    
 