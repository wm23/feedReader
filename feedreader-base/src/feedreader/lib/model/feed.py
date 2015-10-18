__author__ = 'wojtek'

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from feedreader.lib import data

from .base import Base

class Feed(Base):

    name = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    # entries
    # etag
    # link
    # title
    # subtitle
    # updatefrequency
    # updated
    # updated_parsed

    def to_dto(self):

        return data.Feed(
            id = self.id,
            title = self.name,
            subtitle = None,
            etag = None,
            link = None,
            update_frequency = None,
            updated = None,
            updated_parsed = None

        )