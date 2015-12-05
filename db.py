#!/usr/bin/env python
# encoding: utf-8

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import DIR_PATH

DATABASE_FILE = os.path.join(DIR_PATH, 'db.sqlite')

engine = create_engine('sqlite:///' + DATABASE_FILE, echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()
