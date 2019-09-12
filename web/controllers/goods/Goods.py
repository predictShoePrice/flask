# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

route_goods = Blueprint('goods_page', __name__)


@route_goods.route("/index")
def index():
    return render_template("goods/index.html")


@route_goods.route("/info")
def info():
    return render_template("goods/info.html")


@route_goods.route("/set")
def set():
    return render_template("goods/set.html")


@route_goods.route("/cat")
def cat():
    return render_template("goods/cat.html")


@route_goods.route("/cat-set")
def catSet():
    return render_template("goods/cat_set.html")