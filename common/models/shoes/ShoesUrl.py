# coding: utf-8
from sqlalchemy import Column, DateTime, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from application import db, app


class ShoesUrl(db.Model):
    __bind_key__ = 'shoes'
    __tablename__ = 'shoes_url'
    __table_args__ = (
        Index('idx_product_id_source', 'product_id', 'source', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(String(300))
    product_info = Column(String(2048))
    source = Column(String(50))
    status = Column(INTEGER(2), server_default=text("'1'"))
    add_time = Column(DateTime)
    update_time = Column(DateTime)
