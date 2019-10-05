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


@route_api.route("/item/detail", methods=["post"])
def Detail():
    resp = {'code': 200, 'msg': '操作成功~', 'items': {}}
    req = request.values

    query_detail = ShoesDetail.query.filter_by(sku_id=req['sku_id']).first()
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
    resp['items'] = item_dict

    add_time = ShoesPlatform.query.with_entities(ShoesPlatform.add_time).distinct().all()
    add_time = sorted([int(x[0]) for x in add_time])[-1]
    query_platform = ShoesPlatform.query.filter(
        and_(ShoesPlatform.sku_id == req['sku_id'], ShoesPlatform.add_time == add_time)).all()
    platforms = ShoesPlatform.query.with_entities(ShoesPlatform.platform).distinct().all()
    platforms = [x[0] for x in platforms]
    shoe_size = ShoesPlatform.query.with_entities(ShoesPlatform.shoe_size).distinct().all()
    shoe_size = sorted([float(x[0]) for x in shoe_size])
    df = pd.DataFrame(index=platforms, columns=shoe_size)
    for item in query_platform:
        df.at[item.platform, float(item.shoe_size)] = [item.purchase_price, item.platform_price]
    df = np.array(df)
    size_list = []
    for _i in range(3):
        size_list.append({platforms[_i]: df.tolist()[_i]})
    resp['size'] = size_list
    resp['shoe_size'] = shoe_size
    return jsonify(resp)


@route_api.route("/item/trend", methods=["post"])
def ItemTrend():
    resp = {'code': 200, 'msg': '操作成功~', 'items': {}}
    req = request.values

    query_detail = ShoesDetail.query.filter_by(sku_id=req['sku_id']).first()
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
    resp['items'] = item_dict

    add_time = ShoesPlatform.query.with_entities(ShoesPlatform.add_time).distinct().all()
    add_time = sorted([int(x[0]) for x in add_time])[-1]
    query_platform = ShoesPlatform.query.filter(
        and_(ShoesPlatform.sku_id == req['sku_id'], ShoesPlatform.add_time == add_time)).all()
    platforms = ShoesPlatform.query.with_entities(ShoesPlatform.platform).distinct().all()
    platforms = [x[0] for x in platforms]
    shoe_size = ShoesPlatform.query.with_entities(ShoesPlatform.shoe_size).distinct().all()
    shoe_size = sorted([float(x[0]) for x in shoe_size])
    df = pd.DataFrame(index=platforms, columns=shoe_size)
    for item in query_platform:
        df.at[item.platform, float(item.shoe_size)] = [item.purchase_price, item.platform_price]
    df = np.array(df)
    size_list = []
    for _i in range(3):
        size_list.append({platforms[_i]: df.tolist()[_i]})
    resp['size'] = size_list
    resp['shoe_size'] = shoe_size
    return jsonify(resp)
