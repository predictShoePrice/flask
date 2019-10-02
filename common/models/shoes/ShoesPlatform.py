# coding: utf-8
from sqlalchemy import Column, DateTime, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from application import db, app


class ShoesPlatform(db.Model):
    __bind_key__ = 'shoes'
    __tablename__ = 'shoes_platforms'

    id = Column(INTEGER(11), primary_key=True)
    product_key = Column(String(255), unique=True)
    sku_id = Column(String(50))
    platform = Column(String(50))
    purchase_price = Column(String(50))
    platform_price = Column(String(50))
    shoe_size = Column(String(50))
    add_time = Column(String(50))
