# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

class DgPipeline(object):

    config = {
        'user': 'yhh',
        'password': 'yhh@2019',
        'host': '47.111.99.248',
        'database': 'yhh_game',
        'charset':'utf8mb4'
    }

    def process_item(self, item, spider):
        # 将数据存储到GAME_INFO
        # cursor = self.conn.cursor()
        # sql,data = item.save(item)
        # cursor.execute(sql,data)
        # self.conn.commit()
        # cursor.close()
        
        # 将数据更新之 game
        self.update_gameinfo(item)
        return item

    def update_gameinfo(self, item):
        cursor = self.conn.cursor()
        if item:
            if item['title']:
                cursor.execute('SELECT count(1) FROM yhh_game.game where title=%s',[item['title']])
                count = cursor.fetchone()
                if count[0] > 0:                   
                    print("-> 更新折扣游戏")
                    if item.get('rawDiscountPrice'):
                        cursor.execute(
                            '''
                                update yhh_game.game 
                                    set regular_price=%s, discount_price=%s, discount_end=%s,spider_time=%s,percentOff=%s,country_code=%s,country_name=%s,prices=%s
                                where title=%s
                            ''',
                            [
                                item.get('rawRegularPrice'),
                                item.get('rawDiscountPrice'),
                                item.get('discountEndsAt'),
                                datetime.now(),
                                item.get('percentOff'),
                                item.get('title'),
                                item.get('country_code'),
                                item.get('country_name'),
                                item.get('prices')
                            ]
                        )
                else:
                    print("-> 新增游戏信息")
                    cursor.execute(''' 
                        insert into game
                            (country_code,country_name,platform,title,title_zh,url_eshop,regular_price,discount_price,discount_begin,discount_end,spider_time,percentOff,image_url,status,prices) 
                            values 
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,2,%s)                           
                        ''',
                        [
                            item.get('country_code'),
                            item.get('country_name'),
                            item.get('platform'),
                            item.get('title'),
                            item.get('title_zh'),
                            item.get('url_eshop'),
                            item.get('rawRegularPrice'),
                            item.get('rawDiscountPrice'),
                            item.get('discountBeginsAt'),
                            item.get('discountEndsAt'),
                            datetime.now(),
                            item.get('percentOff'),
                            item.get('imageUrl'),
                            item.get('prices')
                        ]
                    )
        self.conn.commit()
        cursor.close()
                

    

    def open_spider(self, spider):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.conn.autocommit = True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def close_spider(self,spider):
        if self.conn:
            self.conn.close()
