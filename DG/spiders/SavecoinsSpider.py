#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import json
from DG.items import GAME_INFO
from datetime import datetime, timedelta
import logging
from scrapy.utils.log import configure_logging


class SavecoinsSpider(scrapy.Spider):
    name = "savecoins"

    def start_requests(self):
        for page in range(1,20): # 20
            yield scrapy.Request(url='https://api-savecoins.nznweb.com.br/v1/games?filter[on_sale]=true&filter[platform]=nintendo&locale=zh-tw&order=popularity_desc&page[number]=%d&page[size]=20&currency=CNY' % page,callback=self.parse,meta={'platform':'switch'})
        for page in range(1,30): # 25    
            yield scrapy.Request(url='https://api-savecoins.nznweb.com.br/v1/games?filter[on_sale]=true&filter[platform]=ps4&locale=zh-tw&order=popularity_desc&page[number]=%d&page[size]=20&currency=CNY' % page,callback=self.parse,meta={'platform':'ps4'})

    def parse(self, response): 
        data = json.loads(response.text)
        game_data = data['data']
        for d in game_data:
            sc = GAME_INFO()
            sc['data_source'] = self.name
            # sc['platform'] = d['platform']
            sc['platform'] = response.meta['platform']
            sc['title'] = d['title']
            sc['releaseDateDisplay'] = datetime.strptime(d['releaseDateDisplay'],'%Y-%m-%d')
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
                    sc['discountBeginsAt'] = datetime.strptime(discountPrice.get('discountBeginsAt','2099-01-01T00:00:00.000Z'),'%Y-%m-%dT%H:%M:%S.000Z')
                    sc['discountEndsAt'] = datetime.strptime(discountPrice.get('discountEndsAt','2099-01-01T00:00:00.000Z'),'%Y-%m-%dT%H:%M:%S.000Z')
                    sc['percentOff'] = discountPrice['percentOff']
            # yield sc
            if sc['title']:
                yield scrapy.Request('https://api-savecoins.nznweb.com.br/v1/games/%s/prices?currency=CNY&locale=zh-tw' % d['slug'], callback=self.parse_price,meta={'gameinfo':sc})

    def parse_price(self,response):
        self.logger.info('Parse function called on %s', response.url)        
        pj = json.loads(response.text);
        prices = []
        for priceInfo in pj['digital']:
            price = priceInfo['priceInfo']
            prices.append({
                'country_name':price['country']['name'], # 国家名称
                'country_code':price['country']['code'], # 国家代码
                'discount_price':price['currentPrice'], # 折扣价格
                'discount_price_raw':price['rawCurrentPrice'], # 折扣价格数字
                # 'hasDiscount':price['hasDiscount'], # 是否折扣
                'regular_price':price['regularPrice']['regularPrice'], #原价
                'regular_price_raw':price['regularPrice']['rawRegularPrice'], #原价数字
                # 'status':price['status'],
                'percentOff':price['discountPrice']['percentOff'] # 折扣率
            })
        response.meta['gameinfo']['prices'] = json.dumps(prices)
        yield response.meta['gameinfo']
