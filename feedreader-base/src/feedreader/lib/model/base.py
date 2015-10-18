__author__ = 'wojtek'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer


class Base(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id =  Column(Integer, primary_key=True, autoincrement= True)

    def to_dto(self):
        raise NotImplementedError("Method to_dto should be overwritten")


Base = declarative_base(cls=Base)
