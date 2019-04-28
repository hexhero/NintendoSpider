# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import time
from datetime import datetime, timedelta

class GAME_INFO(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    platform = scrapy.Field() # 平台
    title = scrapy.Field() # 名称
    title_zh = scrapy.Field() #中午名称
    releaseDateDisplay = scrapy.Field() # 发行日期
    imageUrl = scrapy.Field() # 图片地址
    # price_info 价格信息
    best_price = scrapy.Field() # 是否有优惠
    currentPrice = scrapy.Field() # 当前价格
    rawCurrentPrice = scrapy.Field() # 数字价格
    status = scrapy.Field() # 状态
    url_eshop = scrapy.Field() # 发布地址
    hasDiscount = scrapy.Field() # 是否有打折
    # price info -> country 国家
    country_code = scrapy.Field()
    country_name = scrapy.Field()
    # price info -> regularPrice 正常价
    rawRegularPrice = scrapy.Field() # 正常价格 raw
    regularPrice = scrapy.Field() # 正常价格
    # price info -> discountPrice 打折价
    rawDiscountPrice = scrapy.Field()
    discountPrice = scrapy.Field() # 折扣价格
    discountBeginsAt = scrapy.Field() # 折扣开始时间
    discountEndsAt = scrapy.Field() # 折扣结束时间
    percentOff = scrapy.Field() # 折扣率
    data_source = scrapy.Field() # 数据来源
    def save(self,item):
        add_sql = '''
            INSERT INTO GAME_INFO (
                platform,
                title,
                title_zh,
                release_date,
                best_price,
                current_price,
                status,
                url_eshop,
                discount,
                country_code,
                country_name,
                regular_price,
                discount_price,
                discount_begin,
                discount_end,
                spider_time,
                percentOff,
                image_url,
                data_source
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        
        add_data = [
            item['platform'],
            item['title'],
            item.get('title_zh', None),
            datetime.strptime(item['releaseDateDisplay'],'%Y-%m-%d'),
            item['best_price'],
            item.get('rawCurrentPrice',None),
            item['status'],
            item['url_eshop'],
            item['hasDiscount'],
            item['country_code'],
            item['country_name'],
            item['rawRegularPrice'],
            item.get('rawDiscountPrice',None),
            datetime.strptime(item.get('discountBeginsAt','2099-01-01T00:00:00.000Z'),'%Y-%m-%dT%H:%M:%S.000Z'),
            datetime.strptime(item.get('discountEndsAt','2099-01-01T00:00:00.000Z'),'%Y-%m-%dT%H:%M:%S.000Z'),
            datetime.now(),
            item.get('percentOff',None),
            item.get('imageUrl',None),
            item.get('data_source',None),
        ]
        return add_sql, add_data


