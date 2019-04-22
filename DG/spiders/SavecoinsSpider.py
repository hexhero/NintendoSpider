#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import json
from DG.items import SavecoinsItem

class SavecoinsSpider(scrapy.Spider):
    name = "savecoins"

    def start_requests(self):
        for page in range(1,25):
            yield scrapy.Request(url='https://api-savecoins.nznweb.com.br/v1/games?filter[on_sale]=true&filter[platform]=ps4&locale=zh-tw&order=popularity_desc&page[number]=%d&page[size]=20&currency=CNY' % page,callback=self.parse)
            yield scrapy.Request(url='https://api-savecoins.nznweb.com.br/v1/games?filter[on_sale]=true&filter[platform]=nintendo&locale=zh-tw&order=popularity_desc&page[number]=%d&page[size]=20&currency=CNY' % page,callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        game_data = data['data']
        for d in game_data:
            sc = SavecoinsItem()
            sc['platform'] = d['platform']
            sc['title'] = d['title']
            sc['releaseDateDisplay'] = d['releaseDateDisplay']
            sc['imageUrl'] = d['imageUrl']
            price_info = d.get("price_info",False)
            if price_info:
                sc['best_price'] = price_info['best_price']
                sc['currentPrice'] = price_info['currentPrice']
                sc['rawCurrentPrice'] = price_info['rawCurrentPrice']
                sc['status'] = price_info['status']
                sc['url_eshop'] = price_info['url_eshop']
                sc['hasDiscount'] = price_info['hasDiscount']
                country = price_info.get('country',False)
                if country:
                    sc['country_code'] = country['code']
                    sc['country_name'] = country['name']
                regularPrice = price_info.get('regularPrice',False)
                if regularPrice:
                    sc['rawRegularPrice'] = regularPrice['rawRegularPrice']
                    sc['regularPrice'] = regularPrice['regularPrice']
                discountPrice = price_info.get('discountPrice',False)
                if discountPrice:
                    sc['rawDiscountPrice'] = discountPrice['rawDiscountPrice']
                    sc['discountPrice'] = discountPrice['discountPrice']
                    sc['discountBeginsAt'] = discountPrice['discountBeginsAt']
                    sc['discountEndsAt'] = discountPrice['discountEndsAt']
                    sc['percentOff'] = discountPrice['percentOff']
            yield sc

                    

           