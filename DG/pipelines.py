# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from mysql.connector import errorcode

class DgPipeline(object):

    config = {
        'user': 'yhh',
        'password': 'yhh@2019',
        'host': '47.111.99.248',
        'database': 'yhh_game',
        'charset':'utf8mb4'
    }

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        sql,data = item.save(item)
        cursor.execute(sql,data)
        self.conn.commit()
        cursor.close()
        return item

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
