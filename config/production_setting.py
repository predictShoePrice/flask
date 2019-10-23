# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
# PASSWORD = '0Genius5485'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@118.25.112.15:3306/food_db?charset=utf8'.format(PASSWORD)

MYSQL_PASSWORD = '2019_shoes_stock'
MYSQL_USER = 'root'
MYSQL_HOST = '10.23.123.190'
MYSQL_PORT = '3306'
SQLALCHEMY_DATABASE_URI = \
     'mysql+pymysql://{}:{}@{}:{}/food_db?charset=utf8'. \
         format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SERVER_PORT = 5000
SERVER_HOST = "120.132.7.202"

# RELEASE_VERSION = "20190929001"

SQLALCHEMY_BINDS = {
    'shoes':  'mysql+pymysql://{}:{}@{}:{}/shoes?charset=utf8'. \
         format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT),
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

IGNORE_URLS = [
    "^/user/login",
]

API_IGNORE_URLS = [
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

AUTH_COOKIE_NAME = "mooc_food"

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}

MINA_APP = {
    'appid': 'wx6427c7fafe7d23de',
    'appkey': 'e2814a0f42e947891230bbfbc011f3c3',
    'paykey': 'xxxxxxxxxxxxxx换自己的',
    'mch_id': 'xxxxxxxxxxxx换自己的',
    'callback_url': '/api/order/callback'
}

APP = {
    'domain': 'http://127.0.0.1:5000'
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
