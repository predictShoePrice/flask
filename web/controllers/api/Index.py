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
        item_dict['image_path'] = 'http://soleboard.cn-bj.ufileos.com/' + item.image_path
        item_dict['sale_date'] = item.sale_date
        item_dict['hot_product'] = item.hot_product
        items_list.append(item_dict)
    resp['items'] = items_list
    return jsonify(resp)


@route_api.route("/index/trend", methods=["post"])
def Index_Trend():
    req = request.values

    try:
        method = req['method']
    except:
        resp = {'code': 500, 'msg': '参数缺失: method'}
        return jsonify(resp)

    try:
        trend = req['trend']
    except:
        resp = {'code': 500, 'msg': '参数缺失: trend'}
        return jsonify(resp)

    try:
        page = int(req['page'])
    except:
        resp = {'code': 500, 'msg': '参数缺失: page'}
        return jsonify(resp)

    try:
        num = int(req['num'])
    except:
        num = 10

    if method == 'day':
        if trend == 'up':
            query = ShoesDetail.query.order_by(ShoesDetail.day_trend.desc()) \
                .paginate(page=page, per_page=num, error_out=True, max_per_page=50).items
        else:
            query = ShoesDetail.query.order_by('day_trend').paginate(page=page, per_page=num,
                                                                     error_out=True, max_per_page=50).items
    elif method == 'week':
        if trend == 'up':
            query = ShoesDetail.query.order_by(ShoesDetail.week_trend.desc()) \
                .paginate(page=page, per_page=num, error_out=True, max_per_page=50).items
        else:
            query = ShoesDetail.query.order_by('week_trend').paginate(page=page, per_page=num,
                                                                      error_out=True, max_per_page=50).items
    else:
        query = None

    resp = {'code': 200, 'msg': '操作成功~', 'items': {}, 'page': page}

    items_list = []
    for item in query:
        item_dict = {}
        item_dict['product_id'] = item.product_id
        item_dict['sku_id'] = item.sku_id
        item_dict['product_model'] = item.product_model
        item_dict['product_name'] = item.product_name
        item_dict['initial_price'] = item.initial_price
        item_dict['source'] = item.source
        item_dict['product_url'] = 'http://soleboard.cn-bj.ufileos.com/' + item.product_url
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

    try:
        search = req['query']
    except:
        resp = {'code': 500, 'msg': '参数缺失: query'}
        return jsonify(resp)

    try:
        num = req['num']
    except:
        num = 10

    query = ShoesDetail.query
    rule = or_(ShoesDetail.product_name.ilike("%{0}%".format(search)),
               ShoesDetail.product_model.ilike("%{0}%".format(search)),
               ShoesDetail.sku_id.ilike("%{0}%".format(search)),
               )
    query = query.filter(rule).limit(num).all()
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
        item_dict['image_path'] = 'http://soleboard.cn-bj.ufileos.com/' + item.image_path
        item_dict['sale_date'] = item.sale_date
        item_dict['hot_product'] = item.hot_product
        items_list.append(item_dict)
    resp['items'] = items_list
    return jsonify(resp)
