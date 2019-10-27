# -*- coding: utf-8 -*-
from application import app, db
from common.models.shoes.ShoesQuotes import ShoesQuotes
from common.models.shoes.ShoesPlatform import ShoesPlatform
from common.models.shoes.ShoesDetail import ShoesDetail

'''
python manager.py runjob -m trend/index
'''


class JobTask():
    def __init__(self):
        pass

    def handlePrice(self, quotes):
        try:
            percent_trend = int(((quotes.close - quotes.pre_close) / quotes.pre_close) * 100)
        except:
            percent_trend =0
        print('~~~~~~~~~~~~~~~~~~')
        print(percent_trend)
        sp = ShoesPlatform.query.filter_by(sku_id=quotes.sku, shoe_size=quotes.size, add_time=quotes.time_str)
        for item in sp:
            item.day_trend = percent_trend
            db.session.commit()
        sd = ShoesDetail.query.filter_by(sku_id=quotes.sku)
        for item in sd:
            item.day_trend = percent_trend
            db.session.commit()

    def run(self, params):
        quotes_list = ShoesQuotes.query
        for quotes in quotes_list:
            self.handlePrice(quotes)