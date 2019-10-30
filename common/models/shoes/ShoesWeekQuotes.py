# coding: utf-8
from sqlalchemy import Column, DateTime, Index, String, text, Float
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from application import db, app


class ShoesWeekQuotes(db.Model):
    __bind_key__ = 'shoes'
    __tablename__ = 'shoes_quotes_week'
    __table_args__ = (
        Index('sku_key', unique=True),
    )

    shoe_id = Column(INTEGER)
    sku_key = Column(String(255), primary_key=True)
    sku = Column(String(255))
    size = Column(String(255))
    time_str = Column(String(255))
    time = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
