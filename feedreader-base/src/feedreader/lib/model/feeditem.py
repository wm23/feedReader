__author__ = 'wojtek'


from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .feed import Feed
from feedreader.lib import data

class FeedItem(Base):

    feed_id = Column(Integer, ForeignKey('feed.id'), nullable=False)

    title = Column(String)
    summary = Column(String)
    image_url = Column(String)
    author = Column(String)
    link = Column(String)
    published = Column(Date)
    parsed = Column(Date)

    contents = relationship("FeedItemContent", backref="feed_item")
    tags = relationship("FeedItemTag", backref="feed_item")

    def to_dto(self):
        tags = []
        contents = []

        for tag in self.tags:
            tags.append(tag.to_dto())

        for content in self.contents:
            contents.append(content.to_dto())


        return data.FeedItem(id=self.id,
                             title=self.title,
                             summary=self.summary,
                             image=self.image_url,
                             feed=self.feed_id,
                             contents=contents,
                             author=self.author,
                             link=self.link,
                             published=self.published,
                             parsed=self.parsed,
                             tags=tags)


class FeedItemContent(Base):

    feed_item_id = Column(Integer, ForeignKey('feeditem.id'))
    base = Column(String)
    language = Column(String)
    type = Column(String)
    value = Column(String)

    def to_dto(self):
        return None




class FeedItemTag(Base):

    feed_item_id = Column(Integer, ForeignKey('feeditem.id'))
    name = Column(String)

    def to_dto(self):
        return None
    
