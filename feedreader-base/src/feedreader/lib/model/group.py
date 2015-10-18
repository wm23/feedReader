__author__ = 'wojtek'

from sqlalchemy import Column, Integer, String, Date, ForeignKey

from feedreader.lib.model import Base
from feedreader.lib import data

class Group(Base):

    name = Column(String, nullable=False)
    parrent_group_id = Column(Integer, ForeignKey('group.id'))

    def to_dto(self):
        return data.Group(
            id=self.id,
            name=self.name,
            parrent_group_id=self.parrent_group_id
        )




