#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from db import Base, engine, Session


class GiftList(Base):
    __tablename__ = 'gift_lists'
    id = Column(Integer, primary_key=True)

    #owner =

    name = Column(String(64))


class GiftRequest(Base):
    __tablename__ = 'gift_requests'
    id = Column(Integer, primary_key=True)

    list_id = Column(Integer, ForeignKey('gift_lists.id'))
    list = relationship("GiftList", backref=backref('requests'))
    product_id = Column(Integer, ForeignKey('gift_products.id'))
    product = relationship("GiftProduct")
    # buyer =

    prize = Column(Integer)
    quantity = Column(Integer)
    store = Column(String(512))


class GiftProduct(Base):
    __tablename__ = 'gift_products'

    id = Column(Integer, primary_key=True)

    name = Column(String(64))
    description = Column(String(1024))


# create tables
Base.metadata.create_all(engine)

