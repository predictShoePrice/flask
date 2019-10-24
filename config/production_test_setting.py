# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
PASSWORD = '0Genius5485'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@118.25.112.15:3306/food_db?charset=utf8'.format(PASSWORD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SERVER_PORT = 5000
SERVER_HOST = "0.0.0.0"

RELEASE_VERSION = "20190929001"

SQLALCHEMY_BINDS = {
    'shoes': 'mysql+pymysql://root:{}@118.25.112.15:3306/shoes?charset=utf8'.format(PASSWORD),
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
