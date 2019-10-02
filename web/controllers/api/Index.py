# -*- coding: utf-8 -*-
from web.controllers.api import route_api
from flask import request, jsonify, g
from common.models.shoes.ShoesDetail import ShoesDetail
from sqlalchemy import or_
from common.models.shoes.ShoesPlatform import ShoesPlatform
from common.models.shoes.ShoesUrl import ShoesUrl
from application import app, db
import json


@route_api.route("/index/hot", methods=["get"])
def Index():
    resp = {'code': 200, 'msg': '操作成功~', 'items': {}}
    query = ShoesDetail.query.filter_by(hot_product=1).all()
    items_list = []
    for item in query:
        item_dict = {}
        item_dict['product_id'] = item.product_id
        item_dict['sku_id'] = item.sku_id
        item_dict['product_model'] = item.product_model
        item_dict['product_name'] = item.product_name
        item_dict['initial_price'] = item.initial_price
        item_dict['source'] = item.source
        item_dict['product_url'] = item.product_url
        item_dict['sales_type'] = item.sales_type
        item_dict['image_path'] = item.image_path
        item_dict['sale_date'] = item.sale_date
        item_dict['hot_product'] = item.hot_product
        items_list.append(item_dict)
    resp['items'] = items_list
    return jsonify(resp)


@route_api.route("/index/trend", methods=["post"])
def Trend():
    resp = {'code': 200, 'msg': '操作成功~', 'items': {}}
    req = request.values
    if req['method'] == 'day':
        if req['trend'] == 'up':
            query = ShoesDetail.query.order_by(ShoesDetail.day_trend.desc()).limit(req['num']).all()
        else:
            query = ShoesDetail.query.order_by('day_trend').limit(req['num']).all()
    elif req['method'] == 'week':
        if req['trend'] == 'up':
            query = ShoesDetail.query.order_by(ShoesDetail.week_trend.desc()).limit(req['num']).all()
        else:
            query = ShoesDetail.query.order_by('week_trend').limit(req['num']).all()
    else:
        query = None
    items_list = []
    for item in query:
        item_dict = {}
        item_dict['product_id'] = item.product_id
        item_dict['sku_id'] = item.sku_id
        item_dict['product_model'] = item.product_model
        item_dict['product_name'] = item.product_name
        item_dict['initial_price'] = item.initial_price
        item_dict['source'] = item.source
        item_dict['product_url'] = item.product_url
        item_dict['sales_type'] = item.sales_type
        item_dict['image_path'] = item.image_path
        item_dict['sale_date'] = item.sale_date
        item_dict['hot_product'] = item.hot_product
        item_dict['day_trend'] = item.day_trend
        item_dict['week_trend'] = item.week_trend
        items_list.append(item_dict)
    resp['items'] = items_list
    return jsonify(resp)


@route_api.route("/index/search", methods=["post"])
def Search():
    resp = {'code': 200, 'msg': '操作成功~', 'items': {}}
    req = request.values
    if not req['num']:
        resp['code'] = 404
        resp['msg'] = '错误'
        return jsonify(resp)
    query = ShoesDetail.query
    rule = or_(ShoesDetail.product_name.ilike("%{0}%".format(req['query'])),
               ShoesDetail.product_model.ilike("%{0}%".format(req['query'])))
    query = query.filter(rule).limit(req['num']).all()
    items_list = []
    for item in query:
        item_dict = {}
        item_dict['product_id'] = item.product_id
        item_dict['sku_id'] = item.sku_id
        item_dict['product_model'] = item.product_model
        item_dict['product_name'] = item.product_name
        item_dict['initial_price'] = item.initial_price
        item_dict['source'] = item.source
        item_dict['product_url'] = item.product_url
        item_dict['sales_type'] = item.sales_type
        item_dict['image_path'] = item.image_path
        item_dict['sale_date'] = item.sale_date
        item_dict['hot_product'] = item.hot_product
        items_list.append(item_dict)
    resp['items'] = items_list
    return jsonify(resp)
