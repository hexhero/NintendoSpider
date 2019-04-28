#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import json
from DG.items import GAME_INFO

class JumpSpider(scrapy.Spider):
    name = "jump"
    
    def start_requests(self):
        for page in range(1,50):
            yield scrapy.Request(url='https://switch.vgjump.com/switch/gameDlc/list?ifDiscount=true&all=true&offset=%d&limit=10' % page, callback=self.parse)

    def parse(self, response):
        data = json.load(response.text)
        games = data.data.games
        for game in games:
            sc = GAME_INFO()
            sc['data_source'] = self.name
            sc['platform'] = 'switch'
            sc['title'] = game['title']
            # TODO 需要继续完善游戏数据
            pass
        pass