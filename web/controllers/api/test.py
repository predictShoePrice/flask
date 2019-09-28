# -*- coding: utf-8 -*-
from web.controllers.api import route_api
from flask import request,jsonify,g
from common.models.food.Food import Food
from common.models.member.MemberCart import MemberCart
from common.libs.member.CartService import CartService
from common.libs.Helper import selectFilterObj,getDictFilterField
from common.libs.UrlManager import UrlManager
from application import app,db
import json


@route_api.route("/test/index", methods=["get"])
def testIndex():
    resp = {'code': 200, 'msg': 'test~~'}
    req = request.values
    print(req)
    return jsonify(resp)