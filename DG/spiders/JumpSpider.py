#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import json
from DG.items import GAME_INFO
from datetime import datetime, timedelta

class JumpSpider(scrapy.Spider):
    name = "jump"
    
    def start_requests(self):
        for page in range(1,50):
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
            yield sc

            