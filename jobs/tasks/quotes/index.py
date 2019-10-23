# -*- coding: utf-8 -*-
from application import app,db
from common.models.shoes.ShoesQuotes import ShoesQuotes
from common.models.shoes.ShoesDetail import ShoesDetail
from common.models.shoes.ShoesPlatform import ShoesPlatform
import json,requests,datetime
from common.libs.Helper import getCurrentDate
from sqlalchemy import func


'''
python manager.py runjob -m quotes/index
'''

class JobTask():
    def __init__(self):
        pass
    def run(self,params):
        list = ShoesDetail.query.all()
        today = getCurrentDate()
        for day in range(0,30):
            for item in list:
                self.handleItem(item, today - datetime.timedelta(day))

    def handleItem(self,item, today):
        yesterday = today + datetime.timedelta(-1)
        today_str = getCurrentDate().strftime('%Y%m%d')
        yesterday_str = yesterday.strftime('%Y%m%d')
        
        quotes_set = {}

        # 查询今天的价格
        today_platform_details = ShoesPlatform.query.filter_by(sku_id=item.sku_id, add_time=today_str)
        for platform in today_platform_details:
            sku_key = yesterday_str + ':' + str(item.id) + ':' + item.sku_id + ':' + platform.shoe_size
            quotes = None
            if sku_key in quotes_set:
                quotes = quotes_set.get(sku_key)
            else:
                quotes = ShoesQuotes()
                shoe_id = item.id
                quotes.sku_key = sku_key
                quotes.size = platform.shoe_size
                quotes.sku = item.sku_id
                quotes.time = today
                quotes.time_str = today_str
                quotes.pre_close = 0.0
                price = 0
                if platform.platform_price != '-':
                    price = float(platform.platform_price)
                quotes.open = price
                quotes.high = price
                quotes.low = price
                quotes.close = price
                quotes.volume = 0

            price = quotes.open
            compare_price = 0

            if platform.platform_price != '-':
                compare_price = float(platform.platform_price)
            if compare_price is 0: 
                continue
            if price<= 0.0 or price>compare_price:
                quotes.open = compare_price
                quotes.high = compare_price
                quotes.low = compare_price
                quotes.close = compare_price
            quotes_set[sku_key] = quotes

        # 查询昨天的价格
        yesterday_platform_details = ShoesPlatform.query.filter_by(sku_id=item.sku_id, add_time=yesterday_str)
        for platform in yesterday_platform_details:
            sku_key = yesterday_str + ':' + str(item.id) + ':' + item.sku_id + ':' + platform.shoe_size
            quotes = {}
            if sku_key in quotes_set:
                quotes = quotes_set.get(sku_key)
            else:
                # 今日无行情的直接跳过
                continue

            price = quotes.pre_close
            compare_price = 0
            if platform.platform_price != '-':
                compare_price = float(platform.platform_price)
            if compare_price is 0: 
                continue
            if price<=0.0 or price>compare_price:
                quotes.pre_close = compare_price
            quotes_set[sku_key] = quotes

        for quotes in quotes_set.values():
            db.session.add(quotes)
            db.session.commit()
        return True
