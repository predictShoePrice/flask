# -*- coding: utf-8 -*-
from application import app, db
from common.models.shoes.ShoesQuotes import ShoesQuotes
from common.models.shoes.ShoesWeekQuotes import ShoesWeekQuotes
from common.models.shoes.ShoesDetail import ShoesDetail
import json, requests, datetime
from common.libs.Helper import getCurrentDate
from sqlalchemy import func

'''
python manager.py runjob -m quotes/week
'''


class JobTask():
    def __init__(self):
        pass

    def run(self, params):
        list = ShoesDetail.query.filter_by(sku_id='575441-013').all()
        today = getCurrentDate()
        for item in list:
            for day in range(10):
                self.generateWeekQuotes(item, today - datetime.timedelta(20-day))

    def generateWeekQuotes(self, item, today):
        weekday = today.weekday()
        new_bar = False
        text = f'weekday {weekday}'
        app.logger.info(text)
        # 周一作为周行情的开端
        if weekday == 0:
            new_bar = True
        today_str = today.strftime('%Y%m%d')

        # 查询今天的价格
        day_quotes_set = ShoesQuotes.query.filter_by(sku=item.sku_id, time_str=today_str).all()
        for day_quotes in day_quotes_set:
            if new_bar:
                app.logger.info('new_bar ' + today_str)
                week_quotes = ShoesWeekQuotes(sku_key=day_quotes.sku_key)
                week_quotes.shoe_id = day_quotes.shoe_id
                week_quotes.size = day_quotes.size
                week_quotes.sku = day_quotes.sku
                week_quotes.time = today
                week_quotes.time_str = today_str
                week_quotes.open = day_quotes.open
                week_quotes.high = day_quotes.high
                week_quotes.low = day_quotes.low
                week_quotes.close = day_quotes.close
                week_quotes.volume = day_quotes.volume
            else:
                week_quotes = ShoesWeekQuotes.query.filter_by(sku=item.sku_id, size=day_quotes.size).filter(ShoesWeekQuotes.time<today, ShoesWeekQuotes.time>=(today - datetime.timedelta(7))).first()
                if not week_quotes:
                    app.logger.info('skip ' + today_str)
                    continue
                week_quotes.time = today
                week_quotes.high = max(day_quotes.high, week_quotes.high)
                week_quotes.low = max(day_quotes.low, week_quotes.low)
                week_quotes.close = day_quotes.close
                week_quotes.volume = week_quotes.volume + day_quotes.volume

            db.session.merge(week_quotes)
            db.session.commit()
        
        app.logger.info('[week quotes]finish ' + item.sku_id + ' ' + today_str)

        return True
