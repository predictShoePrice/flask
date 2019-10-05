# -*- coding: utf-8 -*-
from web.controllers.api import route_api
from flask import request, jsonify, g
from sqlalchemy import or_, and_
from common.models.shoes.ShoesDetail import ShoesDetail
from common.models.shoes.ShoesPlatform import ShoesPlatform
from common.models.shoes.ShoesUrl import ShoesUrl
from application import app, db
import json
import pandas as pd
import numpy as np
import datetime


@route_api.route("/item/detail", methods=["get"])
def Detail():
    values = request.values
    sku_id = values['sku_id']
    add_time = values['date']
    if not sku_id:
        resp = {'code': 500, 'msg': '参数缺失: sku_id'}
        return jsonify(resp)

    if not add_time:
        resp = {'code': 500, 'msg': '参数缺失: add_time'}
        return jsonify(resp)

    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}

    query_detail = ShoesDetail.query.filter_by(sku_id=sku_id).first()
    item_dict = {}
    item_dict['product_id'] = query_detail.product_id
    item_dict['sku_id'] = query_detail.sku_id
    item_dict['product_model'] = query_detail.product_model
    item_dict['product_name'] = query_detail.product_name
    item_dict['initial_price'] = query_detail.initial_price
    item_dict['source'] = query_detail.source
    item_dict['product_url'] = query_detail.product_url
    item_dict['sales_type'] = query_detail.sales_type
    item_dict['image_path'] = query_detail.image_path
    item_dict['sale_date'] = query_detail.sale_date
    item_dict['hot_product'] = query_detail.hot_product

    resp['data']['detail'] = item_dict

    # today = datetime.datetime.now()
    # startTime = today - datetime.timedelta(days=7)
    # resp['data']['startTime'] = startTime.strftime("%Y%m%d")

    platforms = ['nice', 'stockx', 'du']
    resp['data']['platforms'] = platforms

    quotes_set = {}
    platform_data = ShoesPlatform.query.filter_by(sku_id=sku_id, add_time=add_time)
    for item in platform_data:
        shoe_size_index = 'index_' + item.shoe_size
        if shoe_size_index in quotes_set:
            quotes = quotes_set[shoe_size_index]
        else:
            quotes = {
                'time': item.add_time,
                'size': item.shoe_size,
                'ask_price': [0,0,0],
                'bid_price': [0,0,0]
            }
            
        platform_index = platforms.index(item.platform)
        if platform_index<0: 
            continue
        quotes['ask_price'][platform_index] = item.purchase_price
        quotes['bid_price'][platform_index] = item.platform_price
        quotes_set[shoe_size_index] = quotes
    resp_quotes = []
    for key in sorted(quotes_set.keys()):
        resp_quotes.append(quotes_set[key])
    resp['data']['quotes'] = resp_quotes
    return jsonify(resp)


@route_api.route("/item/trend", methods=["get"])
def ItemTrend():
    values = request.values
    sku_id = values['sku_id']
    size = values['shoe_size']
    start_time = values['start_time']
    if not sku_id:
        resp = {'code': 500, 'msg': '参数缺失: sku_id'}
        return jsonify(resp)

    if not start_time:
        resp = {'code': 500, 'msg': '参数缺失: start_time (YYYYMMDD)'}
        return jsonify(resp)

    if not size:
        resp = {'code': 500, 'msg': '参数缺失: shoe_size'}
        return jsonify(resp)

    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}

    query_detail = ShoesDetail.query.filter_by(sku_id=sku_id).first()
    item_dict = {}
    item_dict['product_id'] = query_detail.product_id
    item_dict['sku_id'] = query_detail.sku_id
    item_dict['product_model'] = query_detail.product_model
    item_dict['product_name'] = query_detail.product_name
    item_dict['initial_price'] = query_detail.initial_price
    item_dict['source'] = query_detail.source
    item_dict['product_url'] = query_detail.product_url
    item_dict['sales_type'] = query_detail.sales_type
    item_dict['image_path'] = query_detail.image_path
    item_dict['sale_date'] = query_detail.sale_date
    item_dict['hot_product'] = query_detail.hot_product

    resp['data']['detail'] = item_dict

    # today = datetime.datetime.now()
    # startTime = today - datetime.timedelta(days=7)
    # resp['data']['startTime'] = startTime.strftime("%Y%m%d")

    platforms = ['nice', 'stockx', 'du']
    resp['data']['platforms'] = platforms

    quotes_set = {}
    platform_data = ShoesPlatform.query.filter_by(sku_id=sku_id, shoe_size=size).filter(ShoesPlatform.add_time>=start_time)
    for item in platform_data:
        time_index = 'index_' + item.add_time
        if time_index in quotes_set:
            quotes = quotes_set[time_index]
        else:
            quotes = {
                'time': item.add_time,
                'size': item.shoe_size,
                'ask_price': [0,0,0],
                'bid_price': [0,0,0]
            }
            
        platform_index = platforms.index(item.platform)
        if platform_index<0: 
            continue
        quotes['ask_price'][platform_index] = item.purchase_price
        quotes['bid_price'][platform_index] = item.platform_price
        quotes_set[time_index] = quotes
    resp_quotes = []
    for key in sorted(quotes_set.keys()):
        resp_quotes.append(quotes_set[key])
    resp['data']['quotes'] = resp_quotes
    return jsonify(resp)
