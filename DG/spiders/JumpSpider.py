#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import json
from DG.items import GAME_INFO
from datetime import datetime, timedelta

class JumpSpider(scrapy.Spider):
    name = "jump"
    
    def start_requests(self):
        for page in range(1,3): # 30
            yield scrapy.Request(url='https://switch.vgjump.com/switch/gameDlc/list?ifDiscount=true&all=true&offset=%d&limit=10' % (page*10), callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        games = data['data']['games']
        for game in games:
            sc = GAME_INFO()
            sc['data_source'] = self.name
            sc['platform'] = 'switch'
            sc['title'] = game.get('title')
            sc['title_zh'] = game.get('titleZh')
            sc['best_price'] = 1
            sc['rawCurrentPrice'] = game.get('price')
            sc['rawDiscountPrice'] = game.get('price')
            sc['country_name'] = game.get('country')
            sc['rawRegularPrice'] = game.get('priceRaw')
            sc['discountEndsAt'] = datetime.fromtimestamp(game.get('discountEnd')/1000.0) if game.get('discountEnd') else datetime.strptime('2099-1-1 08:00:00', '%Y-%m-%d %H:%M:%S')
            sc['percentOff'] = game.get('cutoff')
            sc['imageUrl'] = game.get('icon')

            if game['appid']:
                yield response.follow('https://switch.vgjump.com/switch/gameInfo?appid=%s' % game['appid'], callback=self.parse_price,meta={'gameinfo':sc})

    def parse_price(self,response):
        info = json.loads(response.text)
        prices = []
        for price in info['data']['prices']:
            prices.append({
                'country_name':price['country'], # 国家名称
                'country_code':price['coinName'], # 国家代码
                'discount_price':price['originPrice'], # 折扣价格
                'discount_price_raw':price['originPrice'], # 折扣价格数字
                # 'hasDiscount':price['hasDiscount'], # 是否折扣
                'regular_price':price['originPrice'], #原价
                'regular_price_raw':price['originPrice'], #原价数字
                'percentOff':price.get('cutoff')
                # 'status':price['status']
            })
        response.meta['gameinfo']['prices'] = json.dumps(prices)
        yield response.meta['gameinfo']
