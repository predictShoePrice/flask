# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import time
import logging
import logging.config
import os

class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path, static_folder=None)
        self.config.from_pyfile('config/local_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        db.init_app(self)

def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates/", root_path=os.getcwd())# -*- coding: utf-8 -*-
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
            percent_trend = (float(quotes.pre_close - quotes.close) / quotes.pre_close) * 100
        except:
            percent_trend = 0
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

CORS(app, supports_credentials=True)
manager = Manager(app)

'''
函数模板
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')

# # 配置日志
logging.config.fileConfig('config/logpain.ini')
