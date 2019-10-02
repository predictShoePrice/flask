# coding: utf-8
from sqlalchemy import Column, DateTime, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ShoesDetail(Base):
    __bind_key__ = 'shoes'
    __tablename__ = 'shoes_detail'
    __table_args__ = (
        Index('idx-product_id', 'sku_id', 'source', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(String(300))
    sku_id = Column(String(300))
    product_model = Column(String(255))
    product_name = Column(String(500))
    initial_price = Column(String(255))
    product_price = Column(String(255))
    source = Column(String(50))
    product_url = Column(String(500))
    product_color = Column(String(255))
    sales_type = Column(String(255))
    image_path = Column(String(255))
    sale_date = Column(String(50))
    add_time = Column(DateTime)
    update_time = Column(DateTime)
